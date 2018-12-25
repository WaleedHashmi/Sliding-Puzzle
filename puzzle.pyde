add_library('minim')
import os, random
path=os.getcwd()

class Tile: 
    def __init__(self,x,y,img,isEmpty):
        self.x = x*(400//nTiles)
        self.y = y*(400//nTiles)
        self.img = img
        self.isEmpty = isEmpty 
        
class Game:
    def __init__(self,w,h,img):
        self.w = w 
        self.h = h 
        self.img = loadImage(path+'/'+img)
        self.board = []
        self.xN = 0 
        self.yN = 0 
        self.xE = 0
        self.xE = 0
        self.randomPos = 0
        self.neighborList = []
        self.temp = []
        self.win = False

        for i in range (nTiles):
            temp = []
            for j in range (nTiles):
                if i==(nTiles - 1) and j==(nTiles - 1): 
                    temp.append (Tile (i,j,loadImage(path+'/black.jpg'),True))
                else:
                    temp.append (Tile (i,j,self.img,False))            
            self.board.append (temp)

    def display (self):
        self.win = self.winCheck()
        if self.win == False:
            for j in range (nTiles):
                for i in range (nTiles):
                    x = self.board[i][j].x
                    y = self.board[i][j].y
                    image (self.board[i][j].img,i*100,j*100,100,100,x,y,x+(400//nTiles),y+(400//nTiles))
                    
        if self.win == True:
            image (loadImage(path+'/img2.png'),0,0,nTiles*100,nTiles*100) 
            #wining  sound
    
    def winCheck(self):
        try:
            matchCount = 0
            for i in range (nTiles):
                for j in range (nTiles): 
                    if self.board[i][j].x == i*(400//nTiles) and self.board[i][j].y == j*(400//nTiles):
                        matchCount += 1
                    print (self.board[i][j].x, i*100, matchCount)
            if matchCount == nTiles**2:
                return True
            return False
        except:
            return False 
            
    def Shuffle(self,shuffles):     
        for s in range (shuffles):         
            # Find the r,c of the empty tile!!
            for j in range (nTiles):
                for i in range (nTiles):
                    if self.board[i][j].isEmpty == True:
                        self.xE = i*100
                        self.yE = j*100        
            
            # Create a list for 4 possible swaps for the empty tile U,D,R,L
            # extract one random position and error-check. 
            self.neighborList = [[0,100],[0,-100],[100,0],[-100,0]]
            self.randomPos = random.randint(0,3)            
            while (self.xE + self.neighborList[self.randomPos][0]) < 0 or (self.xE + self.neighborList[self.randomPos][0]) > 100*(nTiles-1) or (self.yE + self.neighborList[self.randomPos][1]) < 0 or (self.yE + self.neighborList[self.randomPos][1]) > 100*(nTiles-1): 
                self.randomPos = random.randint(0,3)
            self.xN = self.xE + self.neighborList[self.randomPos][0]
            self.yN = self.yE + self.neighborList[self.randomPos][1]
            self.temp = self.board[self.xN/100][self.yN/100]
            self.board[self.xN/100][self.yN/100] = self.board[self.xE/100][self.yE/100]
            self.board[self.xE/100][self.yE/100] = self.temp

    def move (self,mX,mY):
        x = mX//100
        y = mY//100
        for a in [[0,1],[0,-1],[1,0],[-1,0]]:
            if 0<=(x + a[0])<=(nTiles-1) and 0<=(y + a[1])<=(nTiles-1)  and self.board[x + a[0]][y + a[1]].isEmpty == True:
                self.temp = self.board[x + a[0]][y + a[1]]
                self.board[x + a[0]][y + a[1]] = self.board[x][y]
                self.board[x][y] = self.temp 

nTiles = 4 #change the size of the board. entering 5 here would make a 5 x 5 board

newGame =  Game(nTiles*100,nTiles*100,'img.png')

def setup():
    size (newGame.w,newGame.h)
    background (255)
    newGame.Shuffle(150)
    
    #minim = Minim(this) 
    #minim.loadSnippet("background.mp3").loop()

    
def draw():
    newGame.display()

def mouseClicked():
    newGame.move (mouseX,mouseY)
    #minim = Minim(this) 
    #minim.loadSnippet("pika.mp3").play()
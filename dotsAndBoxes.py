#Diego Aspinwall
#12-14-17
#dotsAndBoxes.py

from ggame import *

def buildBoard(): #Should take no arguments. Creates an 4x4 matrix (or whatever size you want) to represent the game board. Each entry in the matrix should be a list of 5 zeros representing the top, bottom, left, right, and center of the square. 
    data['matrix'] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for y in range(0,4):
        for x in range(0,4):
            data['matrix'][y][x] = [0,0,0,0,0]
    print(data['matrix'])


def redrawAll(): #Should take no arguments. Deletes all the graphics on the board (see useful detail #2 below) and draws the current configuration of the board.
    for rw in range(0,5):
        for cl in range(0,5):
            Sprite(dot, (110*cl, 110*rw))
    
    for row in range(0,4):
        for col in range(0,4):
            Sprite(backRectangle, (110*col +10, 110*row +10))

'''
def drawLeftEdge(): #Should take four (or six) arguments, the row and column numbers of the cell that you are working on and the x and y coordinate of the upper lefthand corner. You can also include the coordinates of the bottom righthand corner if you want. This function should draw the edge of the square in the appropriate color.
    
def drawRightEdge(): #See drawLeftEdge
    
def drawTopEdge(): #See drawLeftEdge
    
def drawBottomEdge(): #See drawLeftEdge
    
def drawCenter(): #See drawLeftEdge. The function should color in the center and label it with a 1 or 2 based on who captured it.
    
def drawScore(): #Should take no arguments. The function print the current score as well as detect if the game is over.
    
def updateLeftEdge(): #Should take two arguments, the row and column number of the square that was just clicked. The function should update the matrix for that column to indicate which player clicked the left edge of that box. The function should also update the right edge of the neighboring box if there is one.
    
def updateRightEdge(): #See updateLeftEdge
    
def updateTopEdge(): #See updateLeftEdge
    
def updateBottomEdge(): #See updateLeftEdge
    
def mouseClick(): #Should take one argument, event. The function should figure out where the user clicked (event.x and event.y have the coordinates of the click). The function should figure out which row and column the user clicked and if it is closest to the top edge, bottom edge, left edge, or right edge of the square. The appropriate edge should then be updated.
    
'''

if __name__ == '__main__': #This isn't really a function, but the rest of your code should be in this section. This section should set up the game.
    
    data = {}
    data['matrix'] = 0
    
    blue = Color(0x0000FF,1)
    red = Color(0xFF0000,1)
    gray = Color(0x000000,.5)
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    blackOutline = LineStyle(1,gray)
    
    backRectangle = RectangleAsset(100,100,LineStyle(4,gray),white)
    dot = RectangleAsset(10,10, LineStyle(0,black),black)
    
    redrawAll()
    buildBoard()
    
    App().run()

'''
Useful detail - You will probably want to look at the Matrix Demo to remind yourself how to create and work with a matrix.

Detail #2: To delete all graphics, you can use a for loop.
for item in App().spritelist[:]:
    item.destroy()

Detail #3: Each square should have a matrix associated with it [0,0,0,0,0] = [left, right, top, bottom, center]. When the user clicks a specific space, one of the zeros should change to a 1 or a 2 based on which player clicked.
-------------------------------------------------------
Ideas for extensions:
1) Create some fun animation when someone wins
2) Allow the players to choose the size of the board
3) Allow the players to play multiple games and keep score for the series
4) Create a player vs. computer version
'''
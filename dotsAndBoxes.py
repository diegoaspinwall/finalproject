#Diego Aspinwall
#12-14-17
#dotsAndBoxes.py

'''
Check with Mr. Smed. Not following his exact directions. redrawAll not erasing and doing every click. Show.

'''
from ggame import *

def buildBoard(): #Should take no arguments. Creates an 4x4 matrix (or whatever size you want) to represent the game board. Each entry in the matrix should be a list of 5 zeros representing the top, bottom, left, right, and center of the square. 
    data['matrix'] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #<>x, up down inside second set
    for y in range(0,4):
        for x in range(0,4):
            data['matrix'][y][x] = [0,0,0,0,0]

def redrawAll(): #Should take no arguments. Deletes all the graphics on the board (see useful detail #2 below) and draws the current configuration of the board.
    for item in App().spritelist[:]:
        item.destroy()
    
    for rw in range(0,5):
        for cl in range(0,5):
            Sprite(dot, (110*cl, 110*rw))
    
    for row in range(0,4):
        for col in range(0,5):
            Sprite(verRectangle, (110*col, 110*row+10))
    
    for row in range(0,5):
        for col in range(0,4):
            Sprite(horRectangle, (110*col+10, 110*row))
    

def drawLeftEdge(): #Should take four (or six) arguments, the row and column numbers of the cell that you are working on and the x and y coordinate of the upper lefthand corner. You can also include the coordinates of the bottom righthand corner if you want. This function should draw the edge of the square in the appropriate color.
    for col in range(0,4):
        for row in range(0,4):
            if data['matrix'][col][row][0]==1:
                Sprite(rverRectangle, (110*col, 110*row+10))
            elif data['matrix'][col][row][0]==2:
                Sprite(bverRectangle, (110*col, 110*row+10))
            else:
                Sprite(verRectangle, (110*col, 110*row+10))

def drawRightEdge(): #See drawLeftEdge
    for col in range(1,5):
        for row in range(0,4):
            Sprite(verRectangle, (110*col, 110*row+10))

def drawTopEdge(): #See drawLeftEdge
    for row in range(0,4):
        for col in range(0,4):
            Sprite(horRectangle, (110*col+10, 110*row))

def drawBottomEdge(): #See drawLeftEdge
    for row in range(1,5):
        for col in range(0,4):
            Sprite(horRectangle, (110*col+10, 110*row))


'''
def drawCenter(): #See drawLeftEdge. The function should color in the center and label it with a 1 or 2 based on who captured it.
    
def drawScore(): #Should take no arguments. The function print the current score as well as detect if the game is over.
    
'''
def updateLeftEdge(row,col): #Should take two arguments, the row and column number of the square that was just clicked. The function should update the matrix for that column to indicate which player clicked the left edge of that box. The function should also update the right edge of the neighboring box if there is one.
    if data['matrix'][col][row][0] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][0]=1
        if data['player'] == -1:
            data['matrix'][col][row][0]=2
        data['player'] = (-1)*data['player'] #IF SHARED, BEING SWITCHED TWICE: BAD.
        print(data['matrix'])

def updateRightEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][1] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][1]=1
        if data['player'] == -1:
            data['matrix'][col][row][1]=2
        data['player'] = (-1)*data['player']
        print(data['matrix'])

def updateTopEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][2] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][2]=1
        if data['player'] == -1:
            data['matrix'][col][row][2]=2
        data['player'] = (-1)*data['player']
        print(data['matrix'])

def updateBottomEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][3] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][3]=1
        if data['player'] == -1:
            data['matrix'][col][row][3]=2
        data['player'] = (-1)*data['player']
        print(data['matrix'])

def mouseClick(event): #Should take one argument, event. The function should figure out where the user clicked (event.x and event.y have the coordinates of the click). The function should figure out which row and column the user clicked and if it is closest to the top edge, bottom edge, left edge, or right edge of the square. The appropriate edge should then be updated.
    #print(event.x,event.y)
    
    for col in range(0,4):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                updateLeftEdge(row,col)
                drawLeftEdge()
                print('Left')
    
    for col in range(1,5):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                updateRightEdge(row,col-1)
                print('Right')
    
    for row in range(0,4):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                updateTopEdge(row,col)
                print('Top')
    
    for row in range(1,5):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                updateBottomEdge(row-1,col)
                print('Bottom')
    
    for row in range(0,5):
        for col in range(0,5):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                data['player']=(-1)*data['player']
            if 110*row<event.x<110*row+10 and 10+110*col<event.y<110*(col+1):
                data['player']=(-1)*data['player']
    

if __name__ == '__main__':
    
    data = {}
    data['matrix'] = 0
    data['player'] = 1
    #1 is red, -1 is blue
    
    blue = Color(0x0000FF,1)
    red = Color(0xFF0000,1)
    gray = Color(0x000000,.2)
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    blackOutline = LineStyle(1,gray)
    
    horRectangle = RectangleAsset(100,10,LineStyle(4,gray),white)
    verRectangle = RectangleAsset(10,100,LineStyle(4,gray),white)
    rhorRectangle = RectangleAsset(100,10,LineStyle(4,black),red)
    rverRectangle = RectangleAsset(10,100,LineStyle(4,black),red)
    bhorRectangle = RectangleAsset(100,10,LineStyle(4,black),blue)
    bverRectangle = RectangleAsset(10,100,LineStyle(4,black),blue)
    dot = RectangleAsset(10,10, LineStyle(0,black),black)
    
    buildBoard()
    redrawAll()
    
    App().listenMouseEvent("click", mouseClick)
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
#Diego Aspinwall
#12-14-17
#dotsAndBoxes.py - the third best game ever

from ggame import *

def buildBoard(): #Should take no arguments. Creates an 4x4 matrix (or whatever size you want) to represent the game board. Each entry in the matrix should be a list of 5 zeros representing the top, bottom, left, right, and center of the square. 
    data['matrix'] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #<>x, up and down inside second set
    for y in range(0,4):
        for x in range(0,4):
            data['matrix'][y][x] = [0,0,0,0,0]

def redrawAll(): #Should take no arguments. Deletes all the graphics on the board (see useful detail #2 below) and draws the current configuration of the board.
    for item in App().spritelist[:]:
        item.destroy()
    
    for rw in range(0,5):
        for cl in range(0,5):
            Sprite(dot, (110*cl, 110*rw))
    
    drawLeftEdges()
    drawRightEdges()
    drawTopEdges()
    drawBottomEdges()
    drawCenters()
    

def drawLeftEdges(): #Should take four (or six) arguments, the row and column numbers of the cell that you are working on and the x and y coordinate of the upper lefthand corner. You can also include the coordinates of the bottom righthand corner if you want. This function should draw the edge of the square in the appropriate color.
    for col in range(0,4):
        for row in range(0,4):
            if data['matrix'][col][row][0]==1:
                Sprite(rverRectangle, (110*col, 110*row+10))
            elif data['matrix'][col][row][0]==2:
                Sprite(bverRectangle, (110*col, 110*row+10))
            else:
                Sprite(verRectangle, (110*col, 110*row+10))

def drawRightEdges(): #See drawLeftEdge
    for col in range(0,4):
        for row in range(0,4):
            if data['matrix'][col][row][1]==1:
                Sprite(rverRectangle, (110*(col+1), 110*row+10))
            elif data['matrix'][col][row][1]==2:
                Sprite(bverRectangle, (110*(col+1), 110*row+10))
            else:
                Sprite(verRectangle, (110*(col+1), 110*row+10))

def drawTopEdges(): #See drawLeftEdge
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][2]==1:
                Sprite(rhorRectangle, (110*col+10, 110*row))
            elif data['matrix'][col][row][2]==2:
                Sprite(bhorRectangle, (110*col+10, 110*row))
            else:
                Sprite(horRectangle, (110*col+10, 110*row))

def drawBottomEdges(): #See drawLeftEdge
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][3]==1:
                Sprite(rhorRectangle, (110*col+10, 110*(row+1)))
            elif data['matrix'][col][row][3]==2:
                Sprite(bhorRectangle, (110*col+10, 110*(row+1)))
            else:
                Sprite(horRectangle, (110*col+10, 110*(row+1)))


def drawCenters(): #See drawLeftEdge. The function should color in the center and label it with a 1 or 2 based on who captured it.
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][4]==1:
                Sprite(redSq, (110*col+10, 110*row+10))
                Sprite(one, (110*col+50, 110*row+25))
            if data['matrix'][col][row][4]==2:
                Sprite(blueSq, (110*col+10, 110*row+10))
                Sprite(two, (110*col+50, 110*row+25))

def drawScore(): #Should take no arguments. The function print the current score as well as detect if the game is over.
    print('Coolcat')

def updateLeftEdge(row,col): #Should take two arguments, the row and column number of the square that was just clicked. The function should update the matrix for that column to indicate which player clicked the left edge of that box. The function should also update the right edge of the neighboring box if there is one.
    if data['matrix'][col][row][0] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][0]=1
            if data['matrix'][col][row][2] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 1
                data['score1'] += 1
        if data['player'] == -1:
            data['matrix'][col][row][0]=2
            if data['matrix'][col][row][2] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 2
                data['score2'] += 1

def updateRightEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][1] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][1]=1
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][2] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 1
                data['score1'] += 1
        if data['player'] == -1:
            data['matrix'][col][row][1]=2
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][2] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 2
                data['score2'] += 1

def updateTopEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][2] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][2]=1
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 1
                data['score1'] += 1
        if data['player'] == -1:
            data['matrix'][col][row][2]=2
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][3] != 0:
                data['matrix'][col][row][4] = 2
                data['score2'] += 1

def updateBottomEdge(row,col): #See updateLeftEdge
    if data['matrix'][col][row][3] == 0:
        if data['player'] == 1:
            data['matrix'][col][row][3]=1
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][2] != 0:
                data['matrix'][col][row][4] = 1
                data['score1'] += 1
        if data['player'] == -1:
            data['matrix'][col][row][3]=2
            if data['matrix'][col][row][0] != 0 and data['matrix'][col][row][1] != 0 and data['matrix'][col][row][2] != 0:
                data['matrix'][col][row][4] = 2
                data['score2'] += 1

def mouseClick(event): #Should take one argument, event. The function should figure out where the user clicked (event.x and event.y have the coordinates of the click). The function should figure out which row and column the user clicked and if it is closest to the top edge, bottom edge, left edge, or right edge of the square. The appropriate edge should then be updated.
    for row in range(0,5):
        for col in range(0,5):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                #if data['matrix'][col][row][2] == 0 or data['matrix'][col][3][3] == 0:
                data['player']=(-1)*data['player']
            '''
            -The data['matrix'] isn't the same row and col range because the row and columns don't think around boxes
            -I included the second part of the 'or' to catch the outer layer of the squares
            '''
            if 110*row<event.x<110*row+10 and 10+110*col<event.y<110*(col+1):
                #if data['matrix'][row][col][0] == 0 or data['matrix'][3][col][1] == 0:
                data['player']=(-1)*data['player']
    
    for col in range(0,4):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                updateLeftEdge(row,col)
                redrawAll()
    
    for col in range(1,5):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                updateRightEdge(row,col-1)
                redrawAll()
    
    for row in range(0,4):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                updateTopEdge(row,col)
                redrawAll()
    
    for row in range(1,5):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                updateBottomEdge(row-1,col)
                redrawAll()

'''
data['score1'] += 1
data['scoreTextRed'].destroy()
scoreRed = TextAsset(str(data['score1']),fill=red, style='bold 30pt Times')
data['scoreTextRed'] = Sprite(scoreRed)
'''

'''
data['score2'] += 1
data['scoreTextBlue'].destroy()
scoreBlue = TextAsset(str(data['score2']),fill=red, style='bold 30pt Times')
data['scoreTextRed'] = Sprite(scoreBlue)
'''

if __name__ == '__main__':
    
    data = {}
    data['matrix'] = 0
    data['player'] = -1
    #1 is red or player 1, -1 is blue or player 2
    data['score1'] = 0
    data['score2'] = 0
    
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
    one = TextAsset('1',fill=black,style='bold 40pt Times')
    two = TextAsset('2',fill=black,style='bold 40pt Times')
    redSq = RectangleAsset(100,100, LineStyle(0,black),red)
    blueSq = RectangleAsset(100,100, LineStyle(0,black),blue)
    scoreRed = TextAsset('0', fill=red, style='bold 30pt Times')
    scoreBlue = TextAsset('0', fill=blue, style='bold 30pt Times')
    
    buildBoard()
    redrawAll()
    
    data['scoreTextRed'] = Sprite(scoreRed)
    data['scoreTextBlue'] = Sprite(scoreBlue,(50,0))
    
    App().listenMouseEvent("click", mouseClick)
    App().run(drawScore)

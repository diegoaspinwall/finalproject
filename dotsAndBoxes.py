#Diego Aspinwall
#12-14-17
#dotsAndBoxes.py - just needs a monkey

from ggame import *

def buildBoard():
    data['matrix'] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #<>columns, rows inside second set
    for y in range(0,4):
        for x in range(0,4):
            data['matrix'][y][x] = [0,0,0,0,0]
    #makes the four sides and center of each square

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    #erases the things that were sprited
    for rw in range(0,5):
        for cl in range(0,5):
            Sprite(dot, (110*cl, 110*rw))
    #sprites the dots
    drawLeftEdges()
    drawRightEdges()
    drawTopEdges()
    drawBottomEdges()
    drawCenters()
    drawScore()
    print('BAM')

def drawLeftEdges():
    #goes thru columns and rows and sprites color or blank depending on what was clicked by whom. Same for next four
    for col in range(0,4):
        for row in range(0,4):
            if data['matrix'][col][row][0]==1:
                Sprite(rverRectangle, (110*col, 110*row+10))
            elif data['matrix'][col][row][0]==2:
                Sprite(bverRectangle, (110*col, 110*row+10))
            else:
                Sprite(verRectangle, (110*col, 110*row+10))

def drawRightEdges():
    for col in range(0,4):
        for row in range(0,4):
            if data['matrix'][col][row][1]==1:
                Sprite(rverRectangle, (110*(col+1), 110*row+10))
            elif data['matrix'][col][row][1]==2:
                Sprite(bverRectangle, (110*(col+1), 110*row+10))
            else:
                Sprite(verRectangle, (110*(col+1), 110*row+10))

def drawTopEdges():
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][2]==1:
                Sprite(rhorRectangle, (110*col+10, 110*row))
            elif data['matrix'][col][row][2]==2:
                Sprite(bhorRectangle, (110*col+10, 110*row))
            else:
                Sprite(horRectangle, (110*col+10, 110*row))

def drawBottomEdges():
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][3]==1:
                Sprite(rhorRectangle, (110*col+10, 110*(row+1)))
            elif data['matrix'][col][row][3]==2:
                Sprite(bhorRectangle, (110*col+10, 110*(row+1)))
            else:
                Sprite(horRectangle, (110*col+10, 110*(row+1)))


def drawCenters():
    for row in range(0,4):
        for col in range(0,4):
            if data['matrix'][col][row][4]==1:
                Sprite(redSq, (110*col+10, 110*row+10))
                Sprite(one, (110*col+50, 110*row+25))
            if data['matrix'][col][row][4]==2:
                Sprite(blueSq, (110*col+10, 110*row+10))
                Sprite(two, (110*col+50, 110*row+25))

def drawScore():
    #sprites the scores and displays "Game over" when needed
    Sprite(TextAsset(data['score1'], fill=red, style='bold 30pt Times'), (50,500))
    Sprite(TextAsset(data['score2'], fill=blue, style='bold 30pt Times'),(400,500))
    if data['score1'] + data['score2'] == 16:
        Sprite(over, (140,145))

def updateLeftEdge(row,col):
    #depending on who clicks on a left edge, it updates that left edge and if that move fills in a square, changes the score and the data['matrix']
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

def updateRightEdge(row,col):
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

def updateTopEdge(row,col):
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

def updateBottomEdge(row,col):
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

def mouseClick(event):
    switch = False
    
    #checks to see if click is in clickable places, and available, then updates. Also changes switch to True.
    for col in range(0,4):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                if data['matrix'][col][row][0] == 0:
                    updateLeftEdge(row,col)
                    switch = True
    
    for col in range(1,5):
        for row in range(0,4):
            if 110*col<event.x<110*col+10 and 10+110*row<event.y<110*(row+1):
                if data['matrix'][col-1][row][1] == 0:
                    updateRightEdge(row,col-1)
                    switch = True
    
    for row in range(0,4):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                if data['matrix'][col][row][2] == 0:
                    updateTopEdge(row,col)
                    switch = True
    
    for row in range(1,5):
        for col in range(0,4):
            if 110*row<event.y<110*row+10 and 10+110*col<event.x<110*(col+1):
                if data['matrix'][col][row-1][3] == 0:
                    updateBottomEdge(row-1,col)
                    switch = True
    
    #this switches the player if an available spot is clicked (also accepts a left and a right- two trues don't make a false). It also redraws all
    if switch == True:
        data['player']=(-1)*data['player']
        redrawAll()

#runs game
if __name__ == '__main__':
    
    data = {}
    data['matrix'] = 0
    data['player'] = 1
    #1 is red or player 1, -1 is blue or player 2
    data['score1'] = 0
    data['score2'] = 0
    
    blue = Color(0x0000FF,1)
    red = Color(0xFF0000,1)
    bluel = Color(0x0000FF,.5)
    redl = Color(0xFF0000,.5)
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
    redSq = RectangleAsset(100,100, LineStyle(0,black),redl)
    blueSq = RectangleAsset(100,100, LineStyle(0,black),bluel)
    over = TextAsset('Game Over',fill=white,style='bold 50pt Times')
    
    buildBoard()
    redrawAll()

    App().listenMouseEvent("click", mouseClick)
    App().run()

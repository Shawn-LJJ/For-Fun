import sys
from time import sleep
import copy
import random

def getFieldSize():
    
    while True:
        try:
            xsize = input('Enter horizontal length: ')
            ysize = input('Enter vertical length: ')
            
            if xsize.isnumeric() and int(xsize) > 0 and ysize.isnumeric() and int(ysize) > 0:
                break
            else:
                raise Exception
        except:
            print('Invalid input(s)')
    
    emptyField = []
    
    for _ in range(int(ysize)):
        emptyRow = []
        for _ in range(int(xsize)):
            emptyRow.append(0)
        emptyField.append(emptyRow)
    
    return emptyField


def drawField(field):
    
    s = '\n'
    
    for row in range(len(field)):
        s += ('+---' * len(field[0])) + '+\n'
        for col in range(len(field[0])):
            if not field[row][col]:
                s += '|   '
            else:
                s += '| # '
        s += '|\n'
        
    s += ('+---' * len(field[0])) + '+\n'
    print(s)


def setInitialCells(field):
    
    isRandom = input('Random generate cells? (y/Y) ').upper()
    
    if isRandom == 'Y':
        for row in range(len(field)):
            for col in range(len(field[0])):
                field[row][col] = random.randint(0, 1)
        drawField(field)
    
    else:
        drawField(field)
        coordinates = '1'
        while coordinates:
            
            coordinates = input('Enter the coordinate for a starting cell (for eg. 6 8), empty text will exit: ')
            try:
                xcoord, ycoord = coordinates.split(' ')
                if not xcoord.isnumeric() or not ycoord.isnumeric() or xcoord == '0' or ycoord == '0':
                    raise Exception
                
                field[int(ycoord) - 1][int(xcoord) - 1] = 1

            except:
                if coordinates:
                    print('Invalid input(s)')
                continue
            
            drawField(field)
    

def progression(field):
    
    neighbourValue = copy.deepcopy(field)
    
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col]:
                neighbourValue[row][col] -= 1
                if row != 0:
                    neighbourValue[row - 1][col] += 1
                if row != len(field) - 1:
                    neighbourValue[row + 1][col] += 1
                if col != 0:
                    neighbourValue[row][col - 1] += 1
                if col != len(field[0]) - 1:
                    neighbourValue[row][col + 1] += 1
                if row != 0 and col != 0:
                    neighbourValue[row - 1][col - 1] += 1
                if row != len(field) - 1 and col != len(field[0]) - 1:
                    neighbourValue[row + 1][col + 1] += 1
                if col != 0 and row != len(field) - 1:
                    neighbourValue[row + 1][col - 1] += 1
                if col != len(field[0]) - 1 and row != 0:
                    neighbourValue[row - 1][col + 1] += 1
    
    for row in range(len(field)):
        for col in range(len(field[0])):
            if neighbourValue[row][col] == 3 or neighbourValue[row][col] == 2 and field[row][col] == 1:
                field[row][col] = 1
            else:
                field[row][col] = 0
                
    
def main():
    
    field = getFieldSize()
    
    setInitialCells(field)
        
    try:
        while True:
            
            progression(field)
            
            drawField(field)
            
            sleep(1)
    
    except KeyboardInterrupt:
        sys.exit()
        
main()
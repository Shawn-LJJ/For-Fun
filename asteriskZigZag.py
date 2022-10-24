from time import sleep

numOfAsterisk = int(input('Number of asterisks: '))
numOfSpace = int(input('Number of spaces: '))

s = '*' * numOfAsterisk
direction = 1

while True:
    
    if direction == 1:
        s = ' ' + s

    else:
        s = s[1:]
    
    if s.startswith('*') or s[0:numOfSpace] == ' ' * numOfSpace:
        direction *= -1
    
    print(s)
        
    sleep(0.1)
    

from functools import reduce

while True:
    
    try:
        trails = int(input('Enter number of trails: '))
        probOfSuccess = float(input('Enter the probability of success (0 < x < 1): '))
        
        if trails < 1 or probOfSuccess <= 0 or probOfSuccess >= 1:
            raise Exception
        
        break
    
    except Exception:
        print('Invalid input.')

print(f'\nFormula: X ~ B({trails}, {probOfSuccess})\n')


def calculateProb(n, p):
    
    nChooseR = lambda r : ((reduce(lambda a, b : a * b, range(n - r + 1, n + 1)) / reduce(lambda c, d : c * d, range(1, r + 1))) if r != 0 else 1)
    
    return lambda x : nChooseR(x) * ((1 - p) ** x) * (p ** (n - x))

getProb = calculateProb(trails, probOfSuccess)


def getX(n, Xs):
    
    while True:
        
        try:
            
            userInput = int(input('Enter X value, P(X=?): '))
            
            if userInput < 0 or userInput > n or userInput in Xs:
                
                raise Exception
            
            break
        
        except Exception:
            
            print('Invalid X value or X has already entered if is a multiple value.\n')
    
    return userInput


while True:
    
    option = input('1. Single X value\n2. Multiple X values\n3. Range of X values\n4. Exit\n>> ')
    
    Xvalues = []
    
    if option == '1':
        Xvalues.append(getX(trails, Xvalues))
    
    elif option == '2':
        for _ in range(trails):
            
            Xvalues.append(getX(trails, Xvalues))
            
            print(f'Current X value(s): {Xvalues}')
            
            repeat = input('Do you want to enter another X value? Enter y or Y to continue: ').upper()
            
            if repeat != 'Y':
                
                break
        
        else:
            
            print('Warning, you have entered all the values, the probability will just be 1.')
    
    elif option == '3':
        
        try:
            
            minimum = input('Enter the minimum range value (0 if blank): ')
            maximum = input(f'Enter the maximum range value ({trails} if blank): ')
            
            if not minimum:
                minimum = 0
            if not maximum:
                maximum = trails
            
            Xvalues = list(range(int(minimum), int(maximum)))
        
        except Exception:
            
            print('Invalid minimum or maximum value.\n')
            continue
    
    elif option == '4':
        break
    
    else:
        print('Invalid option.')
        
    answer = reduce(lambda t, y : t + y, map(lambda x : getProb(x), Xvalues))
    
    print(f'\nCalculated probability: {answer}\n')
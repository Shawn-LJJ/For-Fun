def collatzSequence(number):
    
    if number % 2 == 0:
        return number // 2
    
    else:
        return 3 * number + 1

num = float(input('Enter a number: '))
steps = 0

while num != 1:
    
    num = collatzSequence(num)
    steps += 1
    
    print(num)

print('No. of steps: ' + str(steps))
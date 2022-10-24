#do matrix calculation

def displayExpression(expression, values):
    pass

def checkComformable(expression):
        
    operatorIndex = 1

    while operatorIndex < len(expression):
        
        if "times" in expression:
            if expression[operatorIndex] == "times":
                if expression[operatorIndex - 1][1] != expression[operatorIndex + 1][0]:
                    print("Warning, the matrix expression is not comformable, please try again")
                    return False
                
                resultantMatrixOrder = [expression[operatorIndex - 1][0], expression[operatorIndex + 1][1]]
                expression[operatorIndex - 1] = resultantMatrixOrder
                for _ in range(2):
                    expression.pop(operatorIndex)
                
                if "times" not in expression:
                    operatorIndex = -1
                else:
                    operatorIndex -= 2
        else:
            if expression[operatorIndex - 1] != expression[operatorIndex + 1]:
                print("Warning, the matrix expression is not comformable, please try again.")
                return False
        
        operatorIndex += 2
    
    print(f"The resultant expression will be {expression}")
    
    return True

def getMatrix():
    
    expression = []     #even index will store the rows and columns of each matrix, while odd index will store the type of operator
    values = []     #it will contain a list of matrices, with each containing a list of rows
    
    counter = 1
    while True:         #each loop creates a new matrix operand and an operator, although the loop can only end after finishing creating a matrix operand (excluding the first matrix operand)
        
        while True:
            
            matrixOrderList = input(f"\nPlease enter the order for matrix {counter} in this format where m is the number of rows and n is the number of columns: m, n\n>> ").replace(" ", "").split(",")
                        
            if len(matrixOrderList) != 2 or not matrixOrderList[0].isdigit() or not matrixOrderList[1].isdigit() or int(matrixOrderList[0]) == 0 or int(matrixOrderList[1]) == 0:
                print("Please enter the number of rows and columns appropriately.")
                continue
            
            matrixOrder = [int(matrixOrderList[0]), int(matrixOrderList[1])]     
            break                  
     
        expression.append(matrixOrder)
        
        matrixValues = []
        for row in range(matrixOrder[0]):
            
            invalid = True
            while invalid:
                
                rowValueList = input(f"\nPlease enter the values in row {row + 1} in the following manner: a b c d e (where a, b, c, d, e are values in row x with 5 columns)\n>> ").split(" ")
                
                if len(rowValueList) != matrixOrder[1]:
                    print(f"You must have only {matrixOrder[1]} value(s) in this row because that's the column size for this matrix. Please re-enter.")
                    continue
                
                rowValues = []                
                try:
                    for valueStr in rowValueList:
                        rowValues.append(float(valueStr))
                except Exception:
                    print("Please enter the appropriate values")
                    continue
                
                invalid = False
            
            matrixValues.append(rowValues)
            
        values.append(matrixValues)
        
        if len(expression) != 1:
            toExit = str(input("\nDo you want to add more matrix operand? Enter (Y) to add more.\n>> "))           
            if toExit.upper() != "Y":
                break
            
        while True:
            choice = str(input("\nChoose which operator to use.\n1. Addition\n2. Subtraction\n3. Multiplication\n>> "))
            if choice == "1":
                expression.append("add")
                break
            elif choice == "2":
                expression.append("minus")
                break
            elif choice == "3":
                expression.append("times")
                break
            else:
                print("Please enter an appropriate option.")        
        
        counter += 1   
    
    return expression, values

def evaluate(expression, values):
    
    return


def main():
    
    # welcome message
    print("Welcome to the matrix calculator.\n")
    print("To have a matrix expression, you need to have at least two matrices with an operator.\nTo create the first matrix, enter the number of rows and columns for the first matrix, and then their respective values.")
    print("Once done, choose which operation to use: addition, subtraction, or multiplication.\nThen repeat the same process for creating the first matrix to create the second matrix.")
    print("Once you have two matrix operands and an operator, you can decide whether to add more matrices or to stop and evaluate the expression.\n")
    input("Press enter to continue...\n")
    
    repeat = "Y"
    while repeat == "Y":
        
        #matrixExpression consists of the list of the matrix "equation", such as a 2x3 times 3x4. matrixValue consists of the actual value inside all the matrices.
        matrixExpression, matrixValue = getMatrix()
        
        #evaluate the whole expression and output it if the whole matrix expression is comformable
        if checkComformable(matrixExpression):
            evaluate(matrixExpression, matrixValue)
        
        #ask user whether to do the matrix calculation again
        #repeat = input("Do you want to evaluate matrix expression again? Enter (Y) to do again.")
        
        print(matrixExpression)
        print(matrixValue)
        
main()
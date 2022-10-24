import json
import os

def calculateGPA(grades):
    
    gradeToPoint = {
        'A+' : 4,
        'A' : 4,
        'B+' : 3.5,
        'B' : 3,
        'C+' : 2.5,
        'C' : 2,
        'D+' : 1.5,
        'D' : 1
    }
    
    numerator = 0
    denominator = 0
    
    for module in grades:
        numerator += (gradeToPoint[grades[module][0]] * int(grades[module][1]))
        denominator += (4 * int(grades[module][1]))
    
    try:
        print('Your GPA: {}'.format(4 * (numerator / denominator)))
    except ZeroDivisionError:
        print('Warning, there are no modules to calculate.')

def getModule(option, gradesData = None):
    
    addMore = 'Y'
    moduleIndex = 1
    newModules = {}
            
    while addMore == 'Y':
        
        if option == 1:
            moduleName = input('Enter module name: ')
            
            if moduleName in list(gradesData.keys()):
                print('Module name already exists.')
                continue
        else:
            moduleName = 'Module {}'.format(moduleIndex)
            moduleIndex += 1
        
        try:
            creditPoints = input('Enter credit points for {}: '.format(moduleName))
            
            if int(creditPoints) < 1:
                raise Exception
        except:
            print('Invalid credit points.\n')
            continue
        
        try:
            grade = input('Enter the grade for {}: '.format(moduleName)).capitalize()
            
            if grade[0] == 'A' or grade[0] == 'B' or grade[0] == 'C' or grade[0] == 'D':
                if len(grade) == 2:
                    if grade[1] != '+':
                        raise Exception
                elif len(grade) > 2:
                    raise Exception
            else:
                raise Exception
        except:
            print('Invalid grade.\n')
            continue
        
        newModules[moduleName] = [grade, creditPoints]
        
        addMore = input('Do you want to add another module? (y/Y) ').upper()
        print("")
    
    return newModules   

def subMenu(option, gradesData):
    
    originalName = input('Enter the module name that you want to change/delete: ')
        
    if originalName not in list(gradesData.keys()):
        print('Module name not found. Please try again.\n')
        return gradesData
    
    if option == '1':
        
        newName = input('Enter the new module name that you want to change to: ')
        
        if newName in list(gradesData.keys()):
            print('The new module name entered has already exist in the database, please try again.\n')
            return gradesData
        
        gradesData[newName] = gradesData.pop(originalName)
    
    elif option == '2':
                
        try:
            creditPoints = input('Enter credit points for {}: '.format(originalName))
            
            if int(creditPoints) < 1:
                raise Exception
        except:
            print('Invalid credit points.\n')
            return gradesData
        
        gradesData[originalName][1] = creditPoints
    
    elif option == '3':
        
        try:
            grade = input('Enter the grade for {}: '.format(originalName)).capitalize()
            
            if grade[0] == 'A' or grade[0] == 'B' or grade[0] == 'C' or grade[0] == 'D':
                if len(grade) == 2:
                    if grade[1] != '+':
                        raise Exception
                elif len(grade) > 2:
                    raise Exception
            else:
                raise Exception
        except:
            print('Invalid grade.\n')
            return gradesData
        
        gradesData[originalName][0] = grade
    
    elif option == '4':
        confirmation = input('Are you sure you want to delete this module? (Y/y) ').upper()
        print('')
        
        if confirmation == 'Y':
            gradesData.pop(originalName)
    
    else:
        print('Invalid option.\n')
    
    return gradesData


def main():
    
    # format for storing grade for a module:
    # module name : [grades gotten, credit points]
    
    gradesInfoDir = os.path.join(os.path.dirname(__file__), 'grades.json')
    
    with open(gradesInfoDir, 'r') as gradesDataInFile:
        gradesData = json.load(gradesDataInFile)
    
    print("------------------\nGPA calculator\n------------------\n")
    
    option = ''
    
    while option != '6':
        
        print('1. Calculate current GPA\n2. Calculate future possible GPA\n3. Calculate GPA from scratch\n4. Add new module and grade\n5. Show/Edit current module/grade\n6. Exit')
        option = input(">> ")
        print("")
        
        if option == '1':
            
            calculateGPA(gradesData)
        
        elif option == '2':
            
            newModules = getModule(1, gradesData)
            calculateGPA(gradesData | newModules)
        
        elif option == '3':
            
            sampleModules = getModule(2)
            calculateGPA(sampleModules)
        
        elif option == '4':
            
            gradesData |= getModule(1, gradesData)
        
        elif option == '5':
            
            displayAgain = 'Y'
            
            while displayAgain == 'Y':
                
                print('List of all the modules, grades, and credit points in the database:')
                
                for index, module in enumerate(gradesData, 1):
                    print('{}. Module name: {}, Grade: {}, Credit points: {}'.format(index, module, gradesData[module][0], gradesData[module][1]))
                
                print('\n\t1. Change module name\n\t2. Change module credit points\n\t3. Change module grade\n\t4. Delete a module\n\t5. Return main menu')
                subOption = input('\t>> ')
                if subOption == '5':
                    displayAgain = 'N'
                else:
                    gradesData = subMenu(subOption, gradesData)
        
        elif option == '6':
            print('Goodbye')
            
            with open(gradesInfoDir, 'w') as gradesDataInFile:
                json.dump(gradesData, gradesDataInFile)
        
        else:
            print('Invalid option.')

main()
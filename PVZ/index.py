import random

game_vars = {
    'turn' : 0,
    'gold' : 100,
    'zombies_killed' : 0,
    'target_zombies' : 50,
    'threat' : 1,
    'danger' : 1,
}

map_location = []
for _ in range(5):
    row_list = []
    for _ in range(20):
        row_list.append(None)
    map_location.append(row_list)

rowLetters = ['A', 'B', 'C', 'D', 'E']

player_units = {
    'archer' : {
        'shortName' : 'ARCHR',
        'price' : 5,
        'min_damage' : 2,
        'max_damage' : 4,
        'damage_radius' : 1,
        'HP' : 5,
        'interval' : 1
    },
    'wall' : {
        'shortName' : 'WALL ',
        'price' : 3,
        'min_damage' : 0,
        'max_damage' : 0,
        'damage_radius' : 1,
        'HP' : 20,
        'interval' : 1
    },
    'gunner' : {
        'shortName' : 'GUNNR',
        'price' : 12,
        'min_damage' : 8,
        'max_damage' : 12,
        'damage_radius' : 1,
        'HP' : 10,
        'interval' : 1
    },
    'turret' : {
        'shortName' : 'TURRT',
        'price' : 25,
        'min_damage' : 20,
        'max_damage' : 25,
        'damage_radius' : 1,
        'HP' : 35,
        'interval' : 2
    },
    'mine' : {
        'shortName' : 'MINE ',
        'price' : 15,
        'min_damage' : 20,
        'max_damage' : 30,
        'damage_radius' : 3,
        'HP' : 1,
        'interval' : 1
    },
    'artillery' : {
        'shortName' : 'ARTRY',
        'price' : 50,
        'min_damage' : 35,
        'max_damage' : 40,
        'damage_radius' : 3,
        'HP' : 25,
        'interval' : 3
    },
    'advanced wall' : {
        'shortName' : 'ADVWL',
        'price' : 40,
        'min_damage' : 0,
        'max_damage' : 0,
        'damage_radius' : 1,
        'HP' : 100,
        'interval' : 1
    },
    'gold mine' : {
        'shortName' : 'GOLDM',
        'price' : 35,
        'min_damage' : 1,
        'max_damage' : 3,
        'damage_radius' : 1,
        'HP' : 30,
        'interval' : 1
    }
}

enemy_units = {
    'zombie' : {
        'shortName' : 'ZOMBI',
        'min_damage' : 3,
        'max_damage' : 5,
        'range' : 1,
        'HP' : 15,
        'speed' : 1,
        'spawn_unit' : 1,
        'reward' : 3,
        'special_effect' : 0
    },
    'werewolf' : {
        'shortName' : 'WWOLF',
        'min_damage' : 2,
        'max_damage' : 4,
        'range' : 1,
        'HP' : 12,
        'speed' : 2,
        'spawn_unit' : 2,
        'reward' : 4,
        'special_effect' : 0
    },
    'heavy zombie' : {
        'shortName' : 'HVZOM',
        'min_damage' : 5,
        'max_damage' : 7,
        'range' : 1,
        'HP' : 20,
        'speed' : 1,
        'spawn_unit' : 3,
        'reward' : 6,
        'special_effect' : 0
    },
    'spitter' : {
        'shortName' : 'SPITR',
        'min_damage' : 4,
        'max_damage' : 6,
        'range' : 3,
        'HP' : 15,
        'speed' : 1,
        'spawn_unit' : 3,
        'reward' : 6,
        'special_effect' : 0
    },
    'critter' : {
        'shortName' : 'CRITR',
        'min_damage' : 3,
        'max_damage' : 5,
        'range' : 1,
        'HP' : 18,
        'speed' : 3,
        'spawn_unit' : 4,
        'reward' : 7,
        'special_effect' : 0
    },
    'buff zombie' : {
        'shortName' : 'BUFZB',
        'min_damage' : 8,
        'max_damage' : 10,
        'range' : 1,
        'HP' : 30,
        'speed' : 1,
        'spawn_unit' : 5,
        'reward' : 10,
        'special_effect' : 0
    },
    'armed zombie' : {
        'shortName' : 'ARMZB',
        'min_damage' : 7,
        'max_damage' : 9,
        'range' : 4,
        'HP' : 25,
        'speed' : 1,
        'spawn_unit' : 5,
        'reward' : 10,
        'special_effect' : 0
    },
    'runner zombie' : {
        'shortName' : 'RUNZB',
        'min_damage' : 5,
        'max_damage' : 7,
        'range' : 1,
        'HP' : 20,
        'speed' : 3,
        'spawn_unit' : 5,
        'reward' : 8,
        'special_effect' : 0
    },
    'barbarian zombie' : {
        'shortName' : 'BARZB',
        'min_damage' : 10,
        'max_damage' : 12,
        'range' : 1,
        'HP' : 45,
        'speed' : 2,
        'spawn_unit' : 6,
        'reward' : 14,
        'special_effect' : 0
    },
    'bandit' : {
        'shortName' : 'BANDT',
        'min_damage' : 4,
        'max_damage' : 15,
        'range' : 1,
        'HP' : 38,
        'speed' : 4,
        'spawn_unit' : 6,
        'reward' : 13,
        'special_effect' : 1
    },
    'burner' : {
        'shortName' : 'BURNR',
        'min_damage' : 3,
        'max_damage' : 5,
        'range' : 2,
        'HP' : 30,
        'speed' : 1,
        'spawn_unit' : 5,
        'reward' : 11,
        'special_effect' : 2
    },
    'fire spirit' : {
        'shortName' : 'FRSPR',
        'min_damage' : 3,
        'max_damage' : 13,
        'range' : 1,
        'HP' : 30,
        'speed' : 3,
        'spawn_unit' : 6,
        'reward' : 13,
        'special_effect' : 2
    },
    'alpha hog' : {
        'shortName' : 'ALHOG',
        'min_damage' : 13,
        'max_damage' : 16,
        'range' : 1,
        'HP' : 65,
        'speed' : 2,
        'spawn_unit' : 7,
        'reward' : 18,
        'special_effect' : 0
    },
    'witch' : {
        'shortName' : 'WITCH',
        'min_damage' : 9,
        'max_damage' : 11,
        'range' : 3,
        'HP' : 40,
        'speed' : 1,
        'spawn_unit' : 7,
        'reward' : 16,
        'special_effect' : 3
    },    
    'john cena' : {
        'shortName' : 'JOHNC',
        'min_damage' : 20,
        'max_damage' : 23,
        'range' : 1,
        'HP' : 80,
        'speed' : 1,
        'spawn_unit' : 8,
        'reward' : 21,
        'special_effect' : 0
    },    
    'giant' : {
        'shortName' : 'GIANT',
        'min_damage' : 25,
        'max_damage' : 30,
        'range' : 2,
        'HP' : 100,
        'speed' : 1,
        'spawn_unit' : 9,
        'reward' : 25,
        'special_effect' : 0
    }
}

playerUnitAbbrList = []
for playerUnit in player_units:
    playerUnitAbbrList.append(player_units[playerUnit]['shortName'])

enemyUnitAbbrList = []
for enemyUnit in enemy_units:
    enemyUnitAbbrList.append(enemy_units[enemyUnit]['shortName'])



def drawMap():
    
    print('    1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20')
    print(' +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
    
    for row in range(5):
        s = ''
        for subRow in range(3):
            for col in range(20):
                if col == 0 and subRow == 1:
                    s += '{}|'.format(rowLetters[row])
                elif col == 0:
                    s += ' |'
                    
                if map_location[row][col] == None:
                    s += '     |'
                else:
                    lengthOfString = len(map_location[row][col][subRow])
                    if lengthOfString == 3:                        
                        s += ' {} |'.format(map_location[row][col][subRow])
                    elif lengthOfString == 4:                        
                        s += '{} |'.format(map_location[row][col][subRow])
                    else:
                        s += '{}|'.format(map_location[row][col][subRow])
            
            if subRow != 2:
                s += '\n'
            
        print(s)
        print(' +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
               
def buyUnit():
        
    while True:
        print('Choose which unit to purchase:')
        for i, unit in enumerate(player_units, 1):
            print('{}. {} ({} golds)'.format(i, unit.capitalize(), player_units[unit]['price']))
        print('{}. Exit'.format(len(player_units) + 1))
        
        option = input('>> ')
        print('')
        
        if option == str(len(player_units) + 1):
            return None
        
        try:
            unit = list(player_units.keys())[int(option) - 1]
            if game_vars['gold'] < player_units[unit]['price']:
                print('Not enough gold!\n')
            else:
                return unit
        except Exception:
            print('Invalid option.\n')
            
            
def upgradeUnit(row, col):
    pass

def sellUnit(row, col):
    pass

                       
def editMap(option, unit = None):
    
    incorrectPosition = True
    phrases = ['place your new unit', 'upgrade your unit', 'sell your unit']
    
    while incorrectPosition:
        print('Please enter the coordinate on where you want to {}. Eg. A12, C5. Or type exit to exit.'.format(phrases[option]))
        coordinate = input('>> ')
        
        if coordinate.upper() == 'EXIT':
            return
        
        if len(coordinate) == 2:
            row = coordinate[0]
            col = coordinate[1]
        elif len(coordinate) == 3:
            row = coordinate[0]
            col = coordinate[1:3]
        else:
            print('Invalid input.\n')
            continue

        try:
            if map_location[rowLetters.index(row.upper())][int(col) - 1] == None:
                if option == 0:
                    map_location[rowLetters.index(row.upper())][int(col) - 1] = [player_units[unit]['shortName'], 'LVL 1', '{}/{}'.format(player_units[unit]['HP'], player_units[unit]['HP']), 0]
                    incorrectPosition = False
                    game_vars['gold'] -= player_units[unit]['price']
                else:
                    print('Warning, there is no unit at that coordinate. Please enter again.\n')
            else:
                if option == 0:
                    print("Warning, there's a unit at that coordinate. Please enter another location.\n")
                else:
                    if map_location[rowLetters.index(row.upper())][int(col) - 1][0] in playerUnitAbbrList:
                        if option == 1:
                            upgradeUnit(row, col)
                        else:
                            sellUnit(row, col)
                        incorrectPosition = False
                    else:
                        print('Warning, that unit is not a friendly unit.\n')
                    
        except Exception:
            print('Invalid input.\n')
        

def playerAttack():
    
    totalGoldProduced = 0
    splashDamage = []
    
    for row in range(5):
        totalRowDamage = 0
        for col in range(20):
            if map_location[row][col] == None:
                continue
            
            if map_location[row][col][0] == 'GOLDM':
                if map_location[row][col][3] % player_units['gold mine']['interval'] == 0:    
                    totalGoldProduced += random.randint(player_units['gold mine']['min_damage'], player_units['gold mine']['max_damage'])
                    
            elif map_location[row][col][0] in playerUnitAbbrList and map_location[row][col][0] != 'MINE ':
                for fullUnitName in player_units: 
                    if player_units[fullUnitName]['shortName'] == map_location[row][col][0]:
                        break
                    
                if map_location[row][col][3] % player_units[fullUnitName]['interval'] == 0:  
                    totalRowDamage += random.randint(player_units[fullUnitName]['min_damage'], player_units[fullUnitName]['max_damage'])
            
            if map_location[row][col][0] in playerUnitAbbrList:
                map_location[row][col][3] += 1
            
            
        print('Total damage for row {}: {}'.format(rowLetters[row], totalRowDamage))
        
def zombieAdvance():
    pass

def spawnZombie():
    pass
                

def startGame():
    # game cycle:
    # 1. show map and option
    # 2. user choose to buy, upgrade, or remove units, ends turn, save game or exit
    # 3. once user ends turn, player's unit will attack first, enemy take damage and die first
    # 4. after player's unit attack, enemy will then move or attack next, player's unit will take damage and die next
    # 5. cycles back to 1.
    
    gameLoop = True
    
    while gameLoop:    
        
        turnLoop = True
        
        while turnLoop:
            drawMap()
            threatBar = ''
            
            for i in range(1, 11):
                if i <= game_vars['threat']:
                    threatBar += '-'
                else:
                    threatBar += ' '
                    
            print('Turn: {} \tThreat level: [{}]\tDanger level: {} \tMonsters killed: {}'.format(game_vars['turn'], threatBar, game_vars['danger'], game_vars['zombies_killed']))
            print('Gold: {}\n\nGame menu:\n1. Buy unit\n2. Upgrade unit\n3. Sell unit\n4. End turn\n5. Save game\n6. Exit'.format(game_vars['gold']))
            gameChoice = input('>> ')
            print('')
            
            if gameChoice == '1':
                unitBought = buyUnit()
                if unitBought != None:
                    editMap(0, unitBought)
                
            elif gameChoice == '2':
                editMap(1)
            elif gameChoice == '3':
                editMap(2)
            elif gameChoice == '4':
                turnLoop = False
            elif gameChoice == '5':
                saveGame()
            elif gameChoice == '6':
                return
            else:
                print('Invalid option.\n')
        
        playerAttack()
        zombieAdvance()
        spawnZombie()

def main():
    print('Welcome to the tower defense game!\n')
    
    mainMenuLoop = True
    
    while mainMenuLoop:
        print('Main menu:\n1. Start new game\n2. Load game\n3. Quit')
        mainMenuChoice = input('>> ')
        print('')
        
        if mainMenuChoice == '1':
            startGame()
        elif mainMenuChoice == '2':
            loadGame()
        elif mainMenuChoice == '3':
            mainMenuLoop = False
            print('Goodbye')
        else:
            print('Invalid option.\n')

main()
import random

grid = [[[] for _ in range(6)] for _ in range(6)]

for i in range(6):
    grid[0][i] = 'wall'
for i in range(6):
    grid[5][i] = 'wall'
for i in range(6):
    grid[i][0] = 'wall'
for i in range(6):
    grid[i][5] = 'wall'
    
grid1 = [[[] for _ in range(6)] for _ in range(6)]

for i in range(6):
    grid1[0][i] = 'wall'
for i in range(6):
    grid1[5][i] = 'wall'
for i in range(6):
    grid1[i][0] = 'wall'
for i in range(6):
    grid1[i][5] = 'wall'
    
agent = [1, 1]
direction = 'East' 
arrows = 2
path = []

def place_gold():
    empty_cells = [(i, j) for i in range(1, 5) for j in range(1, 5) if not (i == 1 and j == 1) and not (i == 2 and j == 1) and not (i == 1 and j == 2)]
    random_cell = random.choice(empty_cells)
    grid[random_cell[0]][random_cell[1]] = 'gold'

def place_pits():
    empty_cells = [(i, j) for i in range(1, 5) for j in range(1, 5) if not (i == 1 and j == 1) and not (i == 2 and j == 1) and not (i == 1 and j == 2)]
    random.shuffle(empty_cells) 

    for cell in empty_cells:
        if grid[cell[0]][cell[1]] != 'gold' and grid[cell[0]][cell[1]] != 'stench':
            grid[cell[0]][cell[1]] = 'pit'
            
            
            adjacent_cells = [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1]-1), (cell[0], cell[1]+1)]
            for adj_cell in adjacent_cells:
                if adj_cell[0] in range(1, 5) and adj_cell[1] in range(1, 5) and grid[adj_cell[0]][adj_cell[1]] != 'gold':
                    grid[adj_cell[0]][adj_cell[1]] = 'breeze'
            return 

def place_wumpus():
    empty_cells = [(i, j) for i in range(1, 5) for j in range(1, 5) if not (i == 1 and j == 1) and not (i == 2 and j == 1) and not (i == 1 and j == 2)]
    random.shuffle(empty_cells)  
    for cell in empty_cells:
        if grid[cell[0]][cell[1]] != 'gold':
            grid[cell[0]][cell[1]] = 'wumpus'
            
            
            adjacent_cells = [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1]-1), (cell[0], cell[1]+1)]
            for adj_cell in adjacent_cells:
                if adj_cell[0] in range(1, 5) and adj_cell[1] in range(1, 5) and grid[adj_cell[0]][adj_cell[1]] != 'gold':
                    grid[adj_cell[0]][adj_cell[1]] = 'stench'
            return  

    


    
def print_grid():
    max_length = max(len(str(cell)) for row in grid for cell in row)
    line = '+' + '-' * (max_length + 2) + '+'
    print("Grid with initial setup")
    for i, row in enumerate(grid):
        print(line)
        for j, cell in enumerate(row):
            if [i, j] == agent:
                if direction == 'East':
                    print(f'| {"▷":^{max_length}}', end='')
                elif direction == 'North':
                    print(f'| {"△":^{max_length}}', end='')
                elif direction == 'South':
                    print(f'| {"▽":^{max_length}}', end='')
                elif direction == 'West':
                    print(f'| {"◁":^{max_length}}', end='')
            elif cell == 'wall':
                print(f'| {"wall":^{max_length}}', end=' ')
            elif cell == 'wumpus':
                print(f'| {"wumpus":^{max_length}}', end=' ')
            elif cell == 'pit':
                print(f'| {"pit":^{max_length}}', end=' ')
            elif cell == 'stench':
                print(f'| {"stench":^{max_length}}', end=' ')
            elif cell == 'breeze':
                print(f'| {"breeze":^{max_length}}', end=' ')
            else:
                print(f'| {str(cell):^{max_length}}', end=' ')
        print('|')
    print(line)
    print("Grid with updated information")
    for i, row in enumerate(grid1):
        print(line)
        for j, cell in enumerate(row):
            if [i, j] == agent:
                if direction == 'East':
                    print(f'| {"▷":^{max_length}}', end='')
                elif direction == 'North':
                    print(f'| {"△":^{max_length}}', end='')
                elif direction == 'South':
                    print(f'| {"▽":^{max_length}}', end='')
                elif direction == 'West':
                    print(f'| {"◁":^{max_length}}', end='')
            elif cell == 'wall':
                print(f'| {"wall":^{max_length}}', end=' ')
            elif cell == 'wumpus':
                print(f'| {"wumpus":^{max_length}}', end=' ')
            elif cell == 'pit':
                print(f'| {"pit":^{max_length}}', end=' ')
            elif cell == 'stench':
                print(f'| {"stench":^{max_length}}', end=' ')
            elif cell == 'breeze':
                print(f'| {"breeze":^{max_length}}', end=' ')
            else:
                print(f'| {str(cell):^{max_length}}', end=' ')
        print('|')
    print(line)
    print('\n\n')
    
def turnRight():
    global direction
    if direction == 'East':
        direction = 'South'
    elif direction == 'South':
        direction = 'West'
    elif direction == 'West':
        direction = 'North'
    elif direction == 'North':
        direction = 'East'

def turnLeft():
    global direction
    if direction == 'East':
        direction = 'North'
    elif direction == 'North':
        direction = 'West'
    elif direction == 'West':
        direction = 'South'
    elif direction == 'South':
        direction = 'East'
    
    
def goForward():
    global agent, direction, wumpus_position

    next_position = [agent[0], agent[1]]  

    if direction == 'East':
        next_position[1] += 1
    elif direction == 'West':
        next_position[1] -= 1
    elif direction == 'North':
        next_position[0] -= 1
    elif direction == 'South':
        next_position[0] += 1
        
        
    if grid1[next_position[0]][next_position[1]] != 'wall' and grid1[next_position[0]][next_position[1]] != 'wumpus' and grid1[next_position[0]][next_position[1]] != 'pit':
        agent = next_position
    elif grid[next_position[0]][next_position[1]] == 'wumpus':
        shoot()
    elif grid[next_position[0]][next_position[1]] == 'pit':
        if random.random() < 0.5:
            turnRight()
            goForward()
        else:
            turnLeft()
            goForward()
    elif grid[next_position[0]][next_position[1]] == 'wall':
        print("Bump!")
        if random.random() < 0.5:
            turnRight()
            goForward()
        else:
            turnLeft()
            goForward()
    else:
        agent = next_position



                
def shoot():
    global arrows, agent, direction
    if arrows > 0:
        arrows -= 1
        if direction == 'East':
            grid[agent[0]][agent[1]] = []
            grid1[agent[0]][agent[1]] = 'safe'
            grid[agent[0]][agent[1]+1] = []
            if grid[agent[0]-1][agent[1]+1] == 'stench':
                grid[agent[0]-1][agent[1]+1] = []
            if grid[agent[0]+1][agent[1]+1] == 'stench':
                grid[agent[0]+1][agent[1]+1] = []
            if grid[agent[0]][agent[1]+2] == 'stench':
                grid[agent[0]][agent[1]+2] = []
            print('Scream!')
            return
        elif direction == 'West':
            grid[agent[0]][agent[1]] = []
            grid1[agent[0]][agent[1]] = 'safe'
            grid[agent[0]][agent[1]-1] = []
            if grid[agent[0]-1][agent[1]-1] == 'stench':
                grid[agent[0]-1][agent[1]-1] = []
            if grid[agent[0]+1][agent[1]-1] == 'stench':
                grid[agent[0]+1][agent[1]-1] = []
            if grid[agent[0]][agent[1]-2] == 'stench':
                grid[agent[0]][agent[1]-2] = []
            print('Scream!')
            return
        elif direction == 'North':
            grid[agent[0]][agent[1]] = []
            grid1[agent[0]][agent[1]] = 'safe'
            grid[agent[0]-1][agent[1]] = []
            if grid[agent[0]-2][agent[1]-1] == 'stench':
                grid[agent[0]-2][agent[1]-1] = []
            if grid[agent[0]-2][agent[1]+1] == 'stench':
                grid[agent[0]-2][agent[1]+1] = []
            if grid[agent[0]-3][agent[1]] == 'stench':
                grid[agent[0]-3][agent[1]] = []
            print('Scream!')
            return
        elif direction == 'South':
            grid[agent[0]][agent[1]] = []
            grid1[agent[0]][agent[1]] = 'safe'
            grid[agent[0]+1][agent[1]] = []
            if grid[agent[0]+2][agent[1]-1] == 'stench':
                grid[agent[0]+2][agent[1]-1] = []
            if grid[agent[0]+2][agent[1]+1] == 'stench':
                grid[agent[0]+2][agent[1]+1] = []
            if grid[agent[0]+3][agent[1]] == 'stench':
                grid[agent[0]+3][agent[1]] = []
            print('Scream!')
            return
    else:
        print('No more arrows!')


        
def auto_play():
    global agent, direction, wumpus_position, pit_position
    grab_gold = False
    stack = []
    while True:
        print_grid()
        if grid[agent[0]][agent[1]] == 'gold':
            grab_gold = True
            print("glitter!!!")
            grid1[agent[0]][agent[1]] = 'safe'
            goForward()
            continue


        elif grid[agent[0]][agent[1]] == 'breeze':
            print("breeze!!")
            grid1[agent[0]][agent[1]] = 'breeze' 
            goForward()
            stack.append(agent[:])
            continue
            
        elif grid[agent[0]][agent[1]] == 'stench':
            print("stench!!")
            grid1[agent[0]][agent[1]] = 'stench'  
            goForward()
            stack.append(agent[:])
            continue

        elif grid[agent[0]][agent[1]] == 'wumpus':
            print("Dead by wumpus")
            wumpus_position = agent[:]
            grid1[agent[0]][agent[1]] = 'wumpus'
            agent = [1,1]
            direction = 'East'
            stack.clear()
            continue
        
        elif grid[agent[0]][agent[1]] == 'pit':
            print("Dead by pit")
            pit_position = agent[:]
            grid1[agent[0]][agent[1]] = 'pit'  
            agent = [1,1]
            direction = 'East'
            stack.clear()
            continue
            
        elif agent == [1,1] and grab_gold:
            print("Climb! You won the game!")
            break
            
        else:
            grid1[agent[0]][agent[1]] = 'safe'
            goForward()
            


            
place_gold()
place_wumpus()
place_pits()
auto_play()
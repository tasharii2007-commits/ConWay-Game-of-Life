import random, time, copy

Width = 60
Height = 60

# Create a list of list for cells
nextCells = []
for i in range(Width):
    column = []
    for y in range(Height):
        if random.randint(0, 1) == 0:
            column.append('#')  # alive cell
        else:
            column.append(' ')  # dead cell
    nextCells.append(column)

while True:  # Main game loop
    print('\n' * 5)
    currentCells = copy.deepcopy(nextCells)

    # Print current cells
    for y in range(Height):
        for x in range(Width):
            print(currentCells[x][y], end='')
        print()

    # Calculate next step
    for x in range(Width):
        for y in range(Height):
            # Get neighboring coordinates
            leftCoord = (x - 1) % Width
            rightCoord = (x + 1) % Width
            upCoord = (y - 1) % Height
            downCoord = (y + 1) % Height

            # Count living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][upCoord] == '#':
                numNeighbors += 1
            if currentCells[x][upCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][upCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][downCoord] == '#':
                numNeighbors += 1
            if currentCells[x][downCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][downCoord] == '#':
                numNeighbors += 1

            # Apply Conway's rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)

grid = [
    ['D', 'C', 'D'],
    ['D', 'D', 'C'],
    ['C', 'D', 'D']
]

position = [0, 0]
visited = set()


def model_agent(position, grid):
    x, y = position
    rows = len(grid)
    cols = len(grid[0])

    if x < rows and y < cols:
        if grid[x][y] == 'D':
            print(f"Cleaning position ({x}, {y})")
            grid[x][y] = 'C'

        # Mark cordinates as visited
        visited.add((x, y))

        if y < cols - 1:
            y += 1  
        elif x < rows - 1:
            x += 1
            if x % 2 == 0:
                y = 0
            else:
                y = cols - 1
        else:
            print("Finished cleaning the grid.")
            return None
    else:
        print("Position out of bounds!")
        return None

    return [x, y]


while position is not None:
    position = model_agent(position, grid)
    if position:
        print(f"New position: {position}")

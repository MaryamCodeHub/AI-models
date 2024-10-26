grid = [
    ['D', 'C'],
    ['C', 'D'],
    ['D', 'C']
]

position = [0, 0]

def simple_reflex_agent(grid, position):
    x, y = position
    rows=len(grid)                #count the no of rows
    cols = len(grid[0])           #count the no of columns by calculating the elements in a single row as all rows have same element in them

    if x < rows and y < cols:
        if grid[x][y] == 'D':
            print(f"Cleaning position ({x}, {y})")
            grid[x][y] = 'C'      # Clean the current cell

        if y < cols - 1:          # Move to the right
            y += 1


        elif x < rows - 1:
            x += 1
            if x % 2 == 0:           # If the current row is even, start from the left; if odd, start from the right
                y = 0
            else:
                y=cols - 1
        else:
            print("Finished cleaning the grid.")
            return None

    else:
        print("Position out of bounds!")
        return None

    return [x, y]                  # Return the new position

while position is not None:                             # Continue while position is not None
    position = simple_reflex_agent(grid, position)
    if position:                                        # If position is valid, print the new position
        print(f"New position: {position}")

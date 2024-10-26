# AI-models

Simple Reflex Model
Overview
The Simple Reflex Model is one of the foundational concepts in artificial intelligence. It describes an agent that selects actions based solely on the current percept, without considering the history of past states. This model operates under a set of predefined rules and reacts to specific stimuli in the environment.

Key Features
Reactive Behavior: The agent acts in response to its immediate environment.
Simplicity: This model is straightforward to implement, making it ideal for basic tasks.
Rule-Based: Actions are determined by a set of condition-action pairs, where specific conditions trigger specific actions.
Components
Environment: The setting in which the agent operates, typically represented as a grid or maze.
Agent: The entity that perceives the environment and takes actions.
Percepts: Information received from the environment that informs the agent's actions.
Actions: The responses that the agent takes based on its percepts.
Implementation
Code Example
Here's a basic implementation of a Simple Reflex Model in Python:

python
Copy code
grid = [
    ['D', 'C', 'D'],
    ['D', 'D', 'C'],
    ['C', 'D', 'D']
]

position = [0, 0]

def simple_reflex_agent(grid, position):
    x, y = position
    rows = len(grid)
    cols = len(grid[0])

    if grid[x][y] == 'D':
        print(f"Cleaning position ({x}, {y})")
        grid[x][y] = 'C'  # Clean the current cell

    if y < cols - 1:          # Move to the right
        y += 1
    elif x < rows - 1:        # Move to the next row if y reaches the end of row
        x += 1
        y = 0
    else:
        print("Finished cleaning the grid.")
        return None

    return [x, y]  # Return the new position

while position:
    position = simple_reflex_agent(grid, position)
Explanation
Grid Representation: The environment is represented as a 2D list where 'D' indicates dirty cells and 'C' indicates clean cells.
Agent Logic: The agent cleans the current position if it is dirty and decides its next move based on the current position.
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/simple-reflex-model.git
cd simple-reflex-model
Run the script:

bash
Copy code
python simple_reflex_model.py
Conclusion
The Simple Reflex Model is a fundamental AI concept that serves as the basis for more complex decision-making models. It is effective in environments where the situation can be handled through a set of predefined rules and immediate reactions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

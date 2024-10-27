# AI-models

# AI Models Repository

This repository contains code implementations of various AI models, including Simple Reflex Models and Model-Based Reflex Agents.

## Simple Reflex Model

The Simple Reflex Model is a basic AI agent that performs actions based on the current percepts from the environment. It follows a straightforward approach to decision-making, executing a specific action when a certain condition is met.

### Key Features
- Cleans a grid of cells represented as 'D' (dirty) and 'C' (clean).
- Moves through the grid in a defined pattern, ensuring all cells are cleaned.
- Utilizes a simple if-else structure for decision-making.

### Usage
To run the Simple Reflex Model, execute the `simple_reflex_model.py` script. The agent will navigate the grid, cleaning dirty cells as it moves.

## Model-Based Reflex Agent

The Model-Based Reflex Agent extends the capabilities of the Simple Reflex Model by maintaining an internal state of the environment. This allows the agent to keep track of which cells have been cleaned, making it more efficient in navigating the grid.

### Key Features
- Cleans a grid of cells while keeping track of visited positions.
- Adapts its movement pattern based on the current row (zigzag pattern).
- Uses a set to store visited cells, preventing re-cleaning of the same cell.

### Usage
To run the Model-Based Reflex Agent, execute the `model_based_reflex_agent.py` script. The agent will clean the grid while navigating efficiently through each row.

## License
License
This project is licensed under the MIT License - see the LICENSE file for details.

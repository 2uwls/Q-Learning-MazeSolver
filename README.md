# Q-Learning for Maze Traversal
## Project Overview
This project aims to explore mazes using the Q-Learning algorithm. Additionally, it compares the performance of the algorithm by varying the learning rate (α) and discount factor (γ).

## install dependencies
install dependencies opening the terminal, navigating to the MazeGenerator directory, and running

In this project, we are using `python 3.7.9`, `matplotlib==3.5.1`

## Start Guide
To run the project, open the terminal, navigate to the MazeGenerator directory, and run the following command:

`python -m src.quick_start`

This command initializes a maze manager, adds a maze to the manager, solves the maze, and visualizes the results. The maze is solved using the DepthFirstBacktracker algorithm. The maze is displayed in the terminal, and the generation and solution animations are saved to the MazeGenerator directory.

## Execution Flow
- `maze_manager.py` : generate and manage mazes
- `solver.py` : solve mazes using the Q-Learning algorithm
- visualization : visualize the maze and the discovered path(using the `show_solution` function in `maze_manager.py`)

## Maze generation
The maze generation is done using the DepthFirstBacktracker algorithm. The algorithm starts at a random cell and moves in a random direction until it reaches a dead end. When it reaches a dead end, it backtracks to the last cell with unvisited neighbors and continues the process until all cells are visited.

## QLearning Class (in `solver.py`)
The QLearning class implements the Q-Learning algorithm. Its main methods include:
- `init`: Initializes the class and sets the main parameters.
- `initialize_Q`: Initializes Q-values for each state-action pair.
- `solve`: Applies the Q-Learning algorithm to navigate through the maze.
- `get_reward`: Computes the reward for moving from the current state to the next state.
- `q_learning_path`: Searches for a path from the start state to the goal state based on learned Q-values.
- `get_next_state`: Computes the next state considering the current state and action.

## Visualization
The visualization is done using the `show_solution` function in `maze_manager.py`. The function displays the maze and the discovered path. The maze is displayed using ASCII characters, and the path is displayed using colored characters.

<img width="826" alt="image" src="https://github.com/2uwls/Q-Learning-MazeSolver/assets/101469780/9366fe21-866c-4fd3-9346-70e8de417a0c">



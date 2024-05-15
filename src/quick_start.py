from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze
from src.solver import QLearning
import logging
logging.getLogger('matplotlib').setLevel(logging.WARNING)


if __name__ == "__main__":

    manager = MazeManager()
    results = []

    for i in range(3):
        maze = manager.add_maze(20, 20)
        solver = QLearning(maze, episodes=1000, alpha=0.5, gamma=0.9, epsilon=0.1)
        path = solver.solve_q_Learning()
        manager.mazes[maze.id].solution_path = path
        results.append(path)
        print(f"Maze {i + 1}:")
        manager.show_solution(maze.id)
    for i, path in enumerate(results, 1):
        print(f"Maze {i} Path:", path)
        print(f"Maze {i} Cost:", len(path))

    # Experiment with different alpha and gamma values
    epsilon = 0.1
    episodes = 1000
    alpha_manager = MazeManager()
    gamma_manager = MazeManager()

    # For each alpha value
    alpha_results = []
    alpha = 0.2
    maze2 = alpha_manager.add_maze(20, 20)  # Assuming you have a function to generate a random maze
    for i in range(4):
        solver = QLearning(maze2, episodes=1000, alpha=alpha, gamma=0.9, epsilon=0.1)
        path = solver.solve_q_Learning()
        alpha_manager.mazes[maze2.id].solution_path = path
        alpha_results.append(path)
        print(f"Maze (alpha){i + 1}:")
        alpha_manager.show_solution(maze2.id)
        alpha+=0.2
    for i, path in enumerate(alpha_results, 1):
        print(f"Maze {i} Path:", path)
        print(f"Maze {i} Cost:", len(path))

    gamma_results = []
    gamma = 0.2
    maze3 = gamma_manager.add_existing_maze(maze2)
    for i in range(4):
        solver = QLearning(maze3, episodes=1000, alpha=0.5, gamma=gamma, epsilon=0.1)
        path = solver.solve_q_Learning()
        gamma_manager.mazes[maze3.id].solution_path = path
        gamma_results.append(path)
        print(f"Maze (gamma){i + 1}:")
        gamma_manager.show_solution(maze3.id)
        gamma+=0.2

    for i, path in enumerate(gamma_results, 1):
        print(f"Maze {i} Path:", path)
        print(f"Maze {i} Cost:", len(path))
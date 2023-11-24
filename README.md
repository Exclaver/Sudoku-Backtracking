# Sudoku Solver
This Python-based Sudoku Solver utilizes the Pygame library to visually demonstrate the process of solving Sudoku puzzles. It offers an engaging way to watch the backtracking algorithm in action.

<p align="center">
  <img src="https://raw.githubusercontent.com/Horrible22232/Sudoku-Solver/main/fig/python_mTfixgQj3G.gif" alt="Sudoku Solver in Action">
</p>

## Features
- A graphical representation of the Sudoku grid using Pygame.
- Real-time solving animation showcasing the backtracking algorithm.
- Customizable puzzle input for diverse Sudoku challenges.

## Installation
Ensure you have Python installed on your system. Then, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Horrible22232/Sudoku-Solver/

# Navigate to the project directory
cd Sudoku-Solver

# Install Pygame
pip install pygame
```

## Usage
To use the solver, specify your Sudoku puzzle in the `sudoku` array in `run.py` and run the script.

```python
# Example of how to specify a Sudoku puzzle
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ...
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Run the solver
python run.py
```

## How It Works
The solver employs a backtracking algorithm, testing different number combinations to solve the puzzle. The algorithm's progress is visually updated on the grid, giving a real-time view of the solving process.

## Contributing
Contributions are welcome! If you have ideas for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

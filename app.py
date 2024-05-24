import argparse

from pathplanner.algorithm import path_planner

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(map(int, line.split())) for line in file]
    return grid

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Path planner algorithm.")
    parser.add_argument('filename', type=str, help="The filename of the grid file.")
    parser.add_argument('t', type=int, help="Total number of discrete time steps.")
    parser.add_argument('T', type=int, help="Maximum duration of the algorithm in milliseconds.")
    parser.add_argument('--start', type=int, nargs=2, default=[0, 0], help="Starting position of the drone (x, y). Default is (0, 0).")

    args = parser.parse_args()

    grid = read_grid_from_file(args.filename)
    N = len(grid)  # Determine the grid size based on the file

    score, path = path_planner(grid, N, args.t, args.T, tuple(args.start))
    print(f"Most valuable path score and path: {score}, {path}")

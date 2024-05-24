# Path planner
Path planner is a path search algorithm. It finds the most valuable path on the grid.

## Usage

You can run Path planner as a cli app. It expects some inputs that you can provide as a command line parameter.

Input parameters:
| Name | Description |
| ---- | ----------- |
| filename | The filename of the grid file. |
| t | Total number of discrete time steps. |
| T | Maximum duration of the algorithm in milliseconds. |
| --start | Starting position of the drone (x, y). Default is (0, 0). |

How to run it:
```bash
$ python app.py filename t T --start x y
```

Example:

```bash
$ python app.py grid.txt 5 1000 --start 2 2
Most valuable path score and path: 44, [(2, 2), (3, 3), (4, 4), (3, 4), (4, 3), (4, 2)]
```

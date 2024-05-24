import time

# Possible movements (horizontally, vertically, and diagonally)
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def path_planner(grid, N, t, T, start):
    start_time = time.time()

    def in_bounds(x, y):
        return 0 <= x < N and 0 <= y < N

    x, y = start
    total_score = grid[x][y]
    step = 0
    change_rate = 10

    visited = {}
    visited[start] = grid[x][y]

    path = []
    path.append(start)

    while time.time() - start_time < T / 1000.0 and step < t:
        best_value = -1
        best_move = None

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and grid[nx][ny] > best_value:
                if (nx, ny) in visited.keys() and visited[(nx, ny)] == grid[nx][ny]:
                    continue

                best_value = grid[nx][ny]
                best_move = (nx, ny)

        if best_move is None:
            break

        x, y = best_move
        visited[best_move] = grid[x][y]
        path.append(best_move)

        total_score += grid[x][y]
        step += 1

        if step % change_rate == 0:
            for vx, vy in visited.keys():
                grid[vx][vy] += 1

    return total_score, path

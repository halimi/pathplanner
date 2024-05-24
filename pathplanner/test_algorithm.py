import unittest

from .algorithm import path_planner

class TestPathPlanner(unittest.TestCase):

    def test_small_grid(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        N = 2
        t = 3
        T = 1000
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 10)
        self.assertEqual(path, [(0,0), (1,1), (1,0), (0,1)])

    def test_large_grid(self):
        grid = [
            [1,   2,  3,  4,  5],
            [6,   7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        N = 5
        t = 10
        T = 1000
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 190)
        self.assertEqual(path, [(0,0), (1,1), (2,2), (3,3), (4,4), (4,3), (4,2), (4,1), (4,0), (3,1), (3,2)])

    def test_grid_with_same_value(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        N = 5
        t = 10
        T = 1000
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 11)
        self.assertEqual(path, [(0,0), (0,1), (0,2), (0,3), (0,4), (1,3), (1,2), (1,1), (1,0), (2,0), (2,1)])

    def test_step_constraint(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        N = 5
        t = 1
        T = 1000
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 2)
        self.assertEqual(path, [(0,0), (0,1)])

    def test_time_constraint(self):
        grid = [
            [1,   2,  3,  4,  5],
            [6,   7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        N = 5
        t = 10000
        T = 1  # Very short time limit
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertTrue(len(path) < t) # Path length should be less than the max steps

    def test_different_start_position(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        N = 3
        t = 5
        T = 1000
        start = (1, 1)
        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 35)
        self.assertEqual(path, [(1,1), (2,2), (2,1), (2,0), (1,0), (0,1)])

    def test_increased_values(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        N = 5
        t = 11
        T = 1000
        start = (0, 0)

        score, path = path_planner(grid, N, t, T, start)
        self.assertEqual(score, 13) # Should be max step (12) plus 1
        self.assertEqual(len(path), 12)

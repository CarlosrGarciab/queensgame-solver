import unittest

import numpy as np

from solver import board, can_place_queen, solve_queens, validate_board


class SolverTests(unittest.TestCase):
    def test_example_board_has_a_valid_solution(self):
        solution = solve_queens(board)

        self.assertIsNotNone(solution)
        self.assertTrue(np.all(solution.sum(axis=1) == 1))
        self.assertTrue(np.all(solution.sum(axis=0) <= 1))
        self.assertEqual(np.count_nonzero(solution), board.shape[0])

        queen_regions = board[solution == 1]
        self.assertEqual(len(np.unique(queen_regions)), board.shape[0])

        for row, col in zip(*np.where(solution == 1)):
            neighbors = solution[
                max(0, row - 1):row + 2,
                max(0, col - 1):col + 2,
            ]
            self.assertEqual(np.count_nonzero(neighbors), 1)

    def test_unsolvable_board_returns_none(self):
        unsolvable_board = np.zeros((2, 2), dtype=int)

        self.assertIsNone(solve_queens(unsolvable_board))

    def test_invalid_board_raises_value_error(self):
        with self.assertRaises(ValueError):
            validate_board(np.array([1, 2, 3]))

        with self.assertRaises(ValueError):
            solve_queens(np.empty((0, 0), dtype=int))

    def test_occupied_cell_cannot_receive_another_queen(self):
        current_board = np.array([[1, 2], [3, 4]])
        solution = np.array([[1, 0], [0, 0]])

        self.assertFalse(can_place_queen(current_board, solution, 0, 0))


if __name__ == "__main__":
    unittest.main()

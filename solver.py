"""Backtracking solver for Queens Game boards."""

import time
from typing import Optional

import numpy as np


# Each number identifies a different region of the board.
board = np.array([
    [5, 5, 5, 5, 3, 4],
    [5, 5, 5, 3, 3, 3],
    [0, 0, 1, 1, 3, 3],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 2, 2, 1],
    [0, 0, 2, 2, 2, 2],
])


def validate_board(board: np.ndarray) -> None:
    """Raise ValueError when a board cannot be solved by this solver."""
    if board.ndim != 2:
        raise ValueError("El tablero debe ser una matriz de dos dimensiones.")
    if board.shape[0] == 0 or board.shape[1] == 0:
        raise ValueError("El tablero no puede estar vacío.")


def can_place_queen(
    board: np.ndarray,
    board_solved: np.ndarray,
    row: int,
    col: int,
) -> bool:
    """Return whether a queen can be placed at ``row``, ``col``."""
    max_rows, max_cols = board.shape

    if board_solved[row, col] != 0:
        return False

    # Queens cannot occupy adjacent cells, including diagonals.
    for current_row in range(max(0, row - 1), min(max_rows, row + 2)):
        for current_col in range(max(0, col - 1), min(max_cols, col + 2)):
            if board_solved[current_row, current_col] == 1:
                return False

    # There can only be one queen in each column.
    if np.any(board_solved[:, col] == 1):
        return False

    # There can only be one queen in each region.
    current_region = board[row, col]
    if np.any(board_solved[board == current_region] == 1):
        return False

    return True


def _search(
    board: np.ndarray,
    board_solved: np.ndarray,
    row: int,
) -> bool:
    max_rows, max_cols = board.shape
    if row == max_rows:
        return True

    for col in range(max_cols):
        if can_place_queen(board, board_solved, row, col):
            board_solved[row, col] = 1
            if _search(board, board_solved, row + 1):
                return True
            board_solved[row, col] = 0

    return False


def solve_queens(board: np.ndarray) -> Optional[np.ndarray]:
    """Find a valid queen placement, or return ``None`` when none exists."""
    board = np.asarray(board)
    validate_board(board)
    board_solved = np.zeros(board.shape, dtype=int)

    if _search(board, board_solved, 0):
        return board_solved
    return None


def main() -> None:
    start_time = time.perf_counter()
    solution = solve_queens(board)
    elapsed_time = (time.perf_counter() - start_time) * 1000

    if solution is None:
        print("No se encontró solución.")
        return

    print("¡Tablero resuelto con éxito!\n")
    print(solution)
    print(f"\nTiempo de ejecución: {elapsed_time:.4f} ms")


if __name__ == "__main__":
    main()

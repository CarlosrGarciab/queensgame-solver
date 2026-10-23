# Backtracking - Queens Game
import numpy as np
import time

"""
Colores del tablero (board):
0: Azul, 1: Naranja, 2: Lila, 3: Celeste, 4: Marrón, 5: Rojo
"""
board = np.array([
    [0, 0, 1, 1, 4, 4],
    [0, 0, 1, 1, 3, 4],
    [0, 1, 1, 3, 3, 4],
    [0, 1, 2, 2, 3, 3],
    [0, 0, 2, 2, 3, 5],
    [0, 0, 2, 2, 5, 5]
])

max_rows, max_cols = board.shape

"""
Estado de resolución (board_solved):
0: Vacío / No se sabe aún
1: Sí es Reina
"""
board_solved = np.zeros((max_rows, max_cols), dtype=int)

def solve_queens(board, board_solved, row):
    # Si ya pasamos de la última fila, ¡ganamos!
    if row == max_rows:
        return True
    
    # Probar cada columna en la fila actual
    for col in range(max_cols):
        if can_place_queen(board, board_solved, row, col):
            # Colocar reina (1)
            board_solved[row, col] = 1
            
            # Recursión
            if solve_queens(board, board_solved, row + 1):
                return True
            
            # La recursión falló: hacemos backtracking y volvemos a poner la celda en 0 (vacía)
            board_solved[row, col] = 0
    return False

def can_place_queen(board, board_solved, row, col):
    # Verificar que la celda esté vacía (0)
    if board_solved[row, col] == 0:
        
        # 1. Verificar vecinos (1 bloque alrededor)
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (0 <= r < max_rows) and (0 <= c < max_cols):
                    if board_solved[r, c] == 1:
                        return False # Hay una reina vecina
        
        # 2. Verificar la misma columna
        for r in range(max_rows):
            if board_solved[r, col] == 1:
                return False # Ya hay otra reina en esta columna
        
        # 3. Verificar la región de color
        current_color = board[row, col]
        for r in range(max_rows):
            for c in range(max_cols):
                if board[r, c] == current_color and board_solved[r, c] == 1:
                    return False # Ya hay una reina en este color
                    
        return True
    return False

start_time = time.time()

# Ejecutar el algoritmo y mostrar el resultado
if solve_queens(board, board_solved, 0):
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000 # Convertir a ms
    
    print("¡Tablero resuelto con éxito!\n")
    print(board_solved)
    print(f"\nTiempo de ejecución: {elapsed_time:.4f} ms")
else:
    print("No se encontró solución.")
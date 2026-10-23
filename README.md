# Queens Game Solver

Solver en Python para un tablero de Queens Game. El programa busca una
distribución válida de reinas mediante backtracking.

## Requisitos

- Python 3.8 o superior
- NumPy

Instala la dependencia con:

```bash
pip install numpy
```

## Uso

Ejecuta el solver desde la raíz del proyecto:

```bash
python solver.py
```

El módulo también expone `solve_queens(board)`, que devuelve una matriz con
las reinas o `None` si el tablero no tiene solución:

```python
from solver import board, solve_queens

solution = solve_queens(board)
```

Para ejecutar las pruebas:

```bash
python -m unittest discover
```

## Reglas consideradas

El solver coloca una reina por fila y comprueba que:

- No haya otra reina en las celdas vecinas, incluyendo las diagonales
  inmediatas.
- No haya otra reina en la misma columna.
- No haya otra reina dentro de la misma región de color.

El tablero se define directamente en `solver.py` mediante una matriz de
valores numéricos. Cada valor representa una región de color diferente.

## Estructura

```text
.
├── README.md
├── solver.py
└── test_solver.py
```
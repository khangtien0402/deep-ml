import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    det=np.linalg.det(matrix)
    trace=np.trace(matrix)
    return det,trace
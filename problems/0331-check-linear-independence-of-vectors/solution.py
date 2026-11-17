import numpy as np


def is_linearly_independent(vectors: list[list[float]]) -> bool:
  if not vectors:
    return True

  matrix = np.array(vectors)
  # Hạng ma trận bằng đúng số lượng vector (số hàng) thì độc lập tuyến tính
  return bool(np.linalg.matrix_rank(matrix) == len(vectors))
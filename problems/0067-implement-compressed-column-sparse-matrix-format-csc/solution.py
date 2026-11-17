import numpy as np


def compressed_col_sparse_matrix(dense_matrix):
  # Transpose the matrix so column-major traversal becomes row-major traversal
  matrix_T = np.array(dense_matrix).T

  # Find non-zero coordinates on the transposed matrix
  col_idx, row_idx = np.nonzero(matrix_T)

  # Extract non-zero values and row indices
  values = matrix_T[col_idx, row_idx].tolist()
  row_indices = row_idx.tolist()

  # Count non-zeros per column (which are rows in matrix_T) and compute cumulative sum
  counts = np.bincount(col_idx, minlength=matrix_T.shape[0])
  col_ptr = np.concatenate(([0], np.cumsum(counts))).tolist()

  return values, row_indices, col_ptr
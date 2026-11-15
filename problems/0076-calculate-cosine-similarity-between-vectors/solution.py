import numpy as np


def cosine_similarity(v1, v2) -> float:
  v1 = np.asarray(v1, dtype=float)
  v2 = np.asarray(v2, dtype=float)

  if v1.shape != v2.shape:
    return 0.0  # Đổi thành: raise ValueError("Shapes must match") nếu đề yêu cầu báo lỗi

  norm_a = np.linalg.norm(v1)
  norm_b = np.linalg.norm(v2)

  if norm_a == 0 or norm_b == 0:
    return 0.0

  return round(float(np.dot(v1, v2) / (norm_a * norm_b)), 3)
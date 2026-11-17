import numpy as np


def phi_transform(data: list[float], degree: int) -> list[list[float]]:
  if degree < 0 or not data:
    return []

  # N = degree + 1 cột (từ bậc 0 đến bậc degree), increasing=True để xếp từ bậc 0 tăng dần
  return np.vander(data, N=degree + 1, increasing=True).tolist()
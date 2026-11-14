import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    arr=np.array(matrix,dtype=float)
    try:
        return np.linalg.inv(arr).tolist()
    except:
        return None
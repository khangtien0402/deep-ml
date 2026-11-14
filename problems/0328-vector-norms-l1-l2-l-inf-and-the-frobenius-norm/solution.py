import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type=="l1":
        return np.linalg.norm(arr.ravel(), ord=1)
    elif norm_type=="l2":
        return np.linalg.norm(arr.ravel(), ord=2)
    elif norm_type=="linf":
        return np.linalg.norm(arr.ravel(), ord=np.inf)
    else:
        if arr.ndim!=2:
            raise ValueError
        else:
            return np.linalg.norm(arr, ord='fro')
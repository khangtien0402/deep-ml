import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    a=np.array(a)
    b=np.array(b)
    try:
     return (a+b).tolist()
    except:
        return -1
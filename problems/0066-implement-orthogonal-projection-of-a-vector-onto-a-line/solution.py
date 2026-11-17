import numpy as np


def orthogonal_projection(v, L):
    v=np.array(v)
    l=np.array(L)
    scalar=np.dot(v,l)/np.dot(l,l)
    return np.round(scalar*l,3).tolist()
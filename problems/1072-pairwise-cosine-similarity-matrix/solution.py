import numpy as np


def pairwise_cosine_similarity(X):
    X = np.asarray(X, dtype=float)

    # 1. Tính chuẩn L2 của từng hàng (kích thước: (n, 1))
    norms = np.linalg.norm(X, axis=1, keepdims=True)

    # 2. Chuẩn hóa từng hàng về vectơ đơn vị (tránh chia cho 0 bằng tham số where)
    X_norm = np.divide(X, norms, out=np.zeros_like(X), where=norms != 0)

    # 3. Nhân ma trận với chuyển vị của nó để lấy tích vô hướng từng cặp
    S = X_norm @ X_norm.T

    # 4. Làm tròn 4 chữ số thập phân và chuyển về Python nested list
    return np.round(S, 4).tolist()
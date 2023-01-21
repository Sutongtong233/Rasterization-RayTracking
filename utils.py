import numpy as np

def BaryCentric(A, B, C, P):
    S_ABC = np.linalg.norm(np.cross(B-A, C-A))/2
    S_BCP = np.linalg.norm(np.cross(C-B, P-B))/2
    u = S_BCP/S_ABC
    S_ACP = np.linalg.norm(np.cross(C-A, P-A))/2
    v = S_ACP/S_ABC
    S_ABP = np.linalg.norm(np.cross(B-A, P-A))/2
    w = S_ABP/S_ABC
    return u, v, w


import numpy as np

def outcrop_trace(T, enu_point, XYZ):
    # We just need the third row of ENU to SDP matrix
    P_row = T[2, :]

    # Estimate the P coordinate of the outcrop point p1
    p = np.dot(P_row, enu_point)

    # XYZ is (n, m, 3) cube of data
    # np.dot will calculate sum product over last axis of DG and vector p_transform
    # D[i, j] equals np.dot(XYZ[i,j,:], P_row)
    DG = p - np.dot(XYZ, P_row)

    return DG
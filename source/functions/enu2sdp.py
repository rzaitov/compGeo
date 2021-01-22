import numpy as np

def enu2sdp(strike, dip):
    '''
    NOTE: strike and dip should be input in radians
    '''
    # make the transformation matrix from ENU coordinates
    # to SDP coordinates. Eq. 5.10
    sin_str = np.sin(strike)
    cos_str = np.cos(strike)
    sin_dip = np.sin(dip)
    cos_dip = np.cos(dip)
    return np.array([
        [sin_str, cos_str, 0],
        [cos_str*cos_dip, -sin_str*cos_dip, -sin_dip],
        [-cos_str*sin_dip, sin_str*sin_dip, -cos_dip]
    ])

def true_thickness(T, top_enu, base_enu):
    '''
    T – coordinate transformation from ENU to SDP

    top and base are 1 x 3 arrays defining the location
    of top and base points in an ENU coordinate system.
    For each one of these arrays, the first, second
    and third entries are the E, N and U coordinates
    '''
    top_sdp = np.dot(T, top)
    base_sdp = np.dot(T, base)

    # compute the thickness of the unit. Eq. 5.12
    return np.abs(base_sdp[2] - top_sdp[2])
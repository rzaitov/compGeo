import numpy as np
from rotation import rotation_matrix

def great_circle(pole_n, pole_e, pole_d): # old parameters (strike, dip)
	'''
	GreatCircle computes the great circle path of a plane in NED coordinate system

	pole_n, pole_e, pole_d - are direct cosines of the plane pole

	Python function translated from the Matlab function
	GreatCircle in Allmendinger et al. (2012)
	'''
	north = np.array([1, 0, 0]) # this vector will be rotated

	n = 181 # number of angles from 0 to 180
	NED = np.zeros((3, n))

	# To make the great circle, rotate the North vector 180 degrees
	# in increments of 1 degree
	for i in range(0, n):
		rad = np.radians(i)
		# Trace great circle
		R = rotation_matrix(pole_n, pole_e, pole_d, rad)
		NED[:, i] = np.dot(R, north) # write result to ith column of the NED matrix

	return np.where(NED[2,:] < 0, -NED, NED) # invert column if Down coordinate is negative
import math
import numpy as np
from rotation import rotation_matrix

def great_circle(pole_n, pole_e, pole_d): # old parameters (strike, dip)
	'''
	GreatCircle computes the great circle path of a plane in NED coordinate system

	pole_n, pole_e, pole_d - are direct cosines of the plane pole

	Python function translated from the Matlab function
	GreatCircle in Allmendinger et al. (2012)
	'''
	# This vector will trace great circle from South to North pole
	v = np.array([-1, 0, 0])

	n = 181 # number of angles from 0 to 180
	NED = np.zeros((3, n))

	# To make the great circle, rotate the North vector 180 degrees
	# in increments of 1 degree
	for i in range(0, n):
		# we should rotate in different directions for western/eastern poles
		# in order to stay in lower hemisphere
		rad = np.sign(pole_e) * np.radians(i)
		R = rotation_matrix(pole_n, pole_e, pole_d, rad)
		NED[:, i] = np.dot(R, v) # write result to ith column of the NED matrix

	# there could be vectors with negative plunge due to impresice calcualtions
	# have a look at an example https://github.com/rzaitov/compGeo/blob/master/source/notebooks/Unstable_Rotate.ipynb
	mask = NED[2,:] < 0
	NED[2, mask] = 0

	return NED
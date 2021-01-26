import numpy as np
from pole_utils import strike_dip_to_trend_plunge
from rotation import rotation, rotate_axis

def great_circle(strike, dip):
	'''
	GreatCircle computes the great circle path of a plane
	in an equal angle or equal area stereonet of unit radius

	strike = strike of plane
	dip = dip of plane
	sttype = type of stereonet: 0 = equal angle, 1 = equal area
	path = x and y coordinates of points in great circle path
	
	NOTE: strike and dip should be entered in radians.
	
	GreatCircle uses functions StCoordLine, Pole and Rotate
	
	Python function translated from the Matlab function
	GreatCircle in Allmendinger et al. (2012)
	'''
	# Compute the pole to the plane. This will be the axis of
	# rotation to make the great circle
	trda, plga = strike_dip_to_trend_plunge(strike, dip)

	# Now pick the strike line at the intersection of the
	# great circle with the primitive of the stereonet
	trd, plg = strike, 0.0

	n = 181 # number of angles from 0 to 180
	rtrd = np.zeros(n)
	rplg = np.zeros(n)

	# To make the great circle, rotate the line 180 degrees
	# in increments of 1 degree
	for deg in range(0, n):
		# # Avoid joining ends of path
		# if rot[i] == pi:
		# 	rot[i] = rot[i]*0.9999
		# Rotate line
		R = rotation(trda, plga, np.radians(deg))
		rtrd[i], rplg[i] = rotate_axis(R, trd, plg)

	return rtrd, rplg
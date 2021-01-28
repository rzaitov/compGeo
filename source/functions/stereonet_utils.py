import numpy as np
import matplotlib.pyplot as plt
from geogr_to_view import geogr_to_view
from small_circle import small_circle
from great_circle import great_circle
from sph_to_cart import sph_to_cart
from st_coord_line import eq_angle_stereonet_transform

# some constants
pi = np.pi
east = pi / 2.0
west = 3.0 * east

def plot_eq_angle_stereonet(trdv, plgv, intrad):
	# Make a larger figure
	plt.rcParams['figure.figsize'] = [15, 7.5]
	plot_stnet_ref_circle()

	# Number of small circles
	n_circles = int(pi // intrad)

	# small circles start at the North
	trd, plg = 0.0, 0.0
	trd, plg = geogr_to_view(trd, plg, trdv, plgv)

	# Plot small circles
	for i in range(1, n_circles+1):
		cone_angle = i*intrad
		NED_SC = small_circle(trd, plg, cone_angle)
		X, Y = eq_angle_stereonet_transform(NED_SC[0,:], NED_SC[1,:], NED_SC[2,:])
		plt.plot(X, Y, color='gray', linewidth=0.5)

	# Great circles
	for i in range(0, n_circles+1):
		if i <= n_circles:	# Western half
			# Pole of great circle
			trd = west
			plg = i*intrad
		else:				# Eastern half
			# Pole of great circle
			trd = east
			plg = (i-n_circles)*intrad

		trd, plg = geogr_to_view(trd, plg, trdv, plgv)

		pole_n, pole_e, pole_d = sph_to_cart(trd, plg)
		NED_GC = great_circle(pole_n, pole_e, pole_d)

		# Calculate stereonet coordinates of rotated line
		# and add to great circle path
		X, Y = eq_angle_stereonet_transform(NED_GC[0,:], NED_GC[1,:], NED_GC[2,:])

		plt.plot(X, Y, color='gray', linewidth=0.5)

def plot_stnet_ref_circle():
	r = 1.0 # radius pf stereonet
	TH = np.radians(np.arange(0,360,1))
	X = r * np.cos(TH)
	Y = r * np.sin(TH)

	# Make a larger figure
	plt.plot(X,Y, 'k')
	plt.axis([-1, 1, -1, 1])
	plt.axis('equal')
	plt.axis('off')
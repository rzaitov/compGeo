import numpy as np
import matplotlib.pyplot as plt
from geogr_to_view import geogr_to_view
from small_circle import small_circle
from great_circle import great_circle

# some constants
pi = np.pi
east = pi / 2.0
west = 3.0 * east

def plot_stereonet(stereonet, intrad, trdv = 0, plgv = pi / 2):
	# Make a larger figure
	plt.rcParams['figure.figsize'] = [15, 7.5]
	plot_stnet_ref_circle()

	# Number of small circles
	n_circles = int(pi // intrad)

	# small circles start at the North
	trd, plg = 0.0, 0.0
	trd, plg = geogr_to_view(trd, plg, trdv, plgv)

	# Small circles
	for i in range(1, n_circles+1):
		cone_angle = i*intrad
		SC_T, SC_P = small_circle(trd, plg, cone_angle)
		X, Y = stereonet(SC_T, SC_P)
		plt.plot(X, Y, color='gray', linewidth=0.5)

	# Great circles
	for i in range(0, n_circles+1):
		trd, plg = west, i*intrad
		trd, plg = geogr_to_view(trd, plg, trdv, plgv)
		GC_T, CG_P = great_circle(trd, plg)
		X, Y = stereonet(GC_T, CG_P)
		plt.plot(X, Y, color='gray', linewidth=0.5)

def plot_stnet_ref_circle():
	r = 1.0 # radius pf stereonet
	TH = np.radians(np.arange(0, 360, 1))
	X = r * np.cos(TH)
	Y = r * np.sin(TH)

	plt.plot(X,Y, 'k')
	plt.axis([-1, 1, -1, 1])
	plt.axis('equal')
	plt.axis('off')
import numpy as np
import matplotlib.pyplot as plt
from Pole import Pole as Pole
from GeogrToView import GeogrToView
from SmallCircle import SmallCircle
from great_circle import great_circle
from sph_to_cart import sph_to_cart
from st_coord_line import eq_angle_stereonet_transform

pi = np.pi

def plot_eq_angle_stereonet(trdv, plgv, intrad):
	# some constants
	east = pi/2.0
	west = 3.0*east
	
	# Plot stereonet reference circle
	r = 1.0 # radius pf stereonet
	TH = np.arange(0,360,1)*pi/180
	X = r * np.cos(TH)
	Y = r * np.sin(TH)
	
	# Make a larger figure
	plt.rcParams['figure.figsize'] = [15, 7.5]
	plt.plot(X,Y, 'k')
	plt.axis ([-1, 1, -1, 1])
	plt.axis ('equal')
	plt.axis('off')
	
	# Number of small circles
	nCircles = int(pi/(intrad*2.0))
	
	# small circles
	# start at the North
	trd = 0.0
	plg = 0.0
	
	# If view direction is not the default (trdv=0,plgv=90)
	# transform line to view direction
	if trdv != 0.0 and plgv != east:
		trd, plg = GeogrToView(trd,plg,trdv,plgv)
	
	# Plot small circles
	# for i in range(1,nCircles+1):
	# 	coneAngle = i*intrad
	# 	path1, path2, np1, np2 = SmallCircle(trd,plg,coneAngle, 0)
	# 	plt.plot(path1[np.arange(0,np1),0], path1[np.arange(0,np1),1], color='gray',linewidth=0.5)
	# 	if np2 > 0:
	# 		plt.plot(path2[np.arange(0,np2),0], path2[np.arange(0,np2),1], color='gray', linewidth=0.5)
	
	# Great circles
	for i in range(0,nCircles*2+1):
		if i <= nCircles:	# Western half
			# Pole of great circle
			trd = west
			plg = i*intrad
		else:				# Eastern half
			# Pole of great circle
			trd = east
			plg = (i-nCircles)*intrad

		# If view direction is not the default 
		# (trdv = 0,plgv = 90)
		# transform line to view direction
		if trdv != 0.0 and plgv != east:
			trd, plg = GeogrToView(trd,plg,trdv,plgv)

		pole_n, pole_e, pole_d = sph_to_cart(trd, plg)
		NED = great_circle(pole_n, pole_e, pole_d)
		NED = NED[:, 1:-1] # skip first and last point of the great circle (pole points)
		                   # due to precision issues these points make a glitch

		# Calculate stereonet coordinates of rotated line
		# and add to great circle path
		X, Y = eq_angle_stereonet_transform(NED[0,:], NED[1,:], NED[2,:])

		plt.plot(X, Y, color='gray', linewidth=0.5)
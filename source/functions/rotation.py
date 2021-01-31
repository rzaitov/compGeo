import numpy as np
from sph_to_cart import sph_to_cart
from cart_to_sph import cart_to_sph

# TODO: depreacated
def rotation(rtrd, rplg, rot):
	# Convert rotation axis to direction cosines. The
	# convention here is X1 = North, X2 = East, X3 = Down
	cn, ce, cd = sph_to_cart(rtrd, rplg)
	return rotation_matrix(cn, ce, cd, rot)

def rotation_matrix(axis_n, axis_e, axis_d, rot):
	# Calculate the transformation matrix a for the rotation
	# Eq. 5.17
	x = 1.0 - np.cos(rot)
	sin_rot = np.sin(rot)
	cos_rot = np.cos(rot)
	return np.array([
		[ cos_rot + axis_n*axis_n*x, -axis_d*sin_rot + axis_n*axis_e*x, axis_e*sin_rot + axis_n*axis_d*x ],
		[ axis_d*sin_rot + axis_e*axis_n*x, cos_rot + axis_e*axis_e*x, -axis_n*sin_rot + axis_e*axis_d*x ],
		[ -axis_e*sin_rot + axis_d*axis_n*x, axis_n*sin_rot + axis_d*axis_e*x, cos_rot + axis_d*axis_d*x ]
	])


def rotate_line(T, trd, plg):
	cned = np.array(sph_to_cart(trd, plg))
	cn, ce, cd = np.dot(T, cned)
	return cart_to_sph(cn, ce, cd)

def rotate_axis(T, trd, plg):
	cned = np.array(sph_to_cart(trd, plg))
	rotated_cned = np.dot(T, cned)
	if rotated_cned[2] < 0:
		rotated_cned *= -1
	cn, ce, cd = rotated_cned
	return cart_to_sph(cn, ce, cd)
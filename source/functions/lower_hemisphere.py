import numpy as np
from zero_two_pi import zero_two_pi

# Take care of negative plunges
def lower_hemisphere(trd, plg):
	condition = plg < 0
	trd = np.where(condition, zero_two_pi(trd + np.pi), trd)
	plg = np.where(condition, -plg, plg)
	return trd, plg
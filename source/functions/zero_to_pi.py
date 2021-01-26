import math
h = 2 * math.pi

# This methog could accept number or numpy array
# Here we exploit that integer division in Python rounds down (not a truncation as in other languages such as C or C++)
# https://docs.python.org/3/library/operator.html#operator.floordiv
def zero_two_pi(a):
	return a - (a // h) * h
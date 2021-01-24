import math

# Proposed API. There is no k parameter.
# Here we follow python's name conventions for functions (all lower case with underscore)
def sph_to_cart(trd, plg):
    cn = math.cos(trd) * math.cos(plg)
    ce = math.sin(trd) * math.cos(plg)
    cd = math.sin(plg)
    return cn, ce, cd
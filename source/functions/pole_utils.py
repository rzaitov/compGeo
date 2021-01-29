import numpy as np
from zero_two_pi import zero_two_pi

east = np.pi/2

# def tp2sd(trd, plg) – maybe shorter name is a better one
def trend_plunge_to_strike_dip(trend, plunge):
  condition = (plunge >= 0)
  dip = np.where(condition, east - plunge, east + plunge)
  strike = np.where(condition, trend + east, trend - east)
  strike = zero_two_pi(strike)
  return strike, dip

# def sd2tp(strike, dip)
def strike_dip_to_trend_plunge(strike, dip):
  plunge = east - dip;
  trend = zero_two_pi(strike - east)
  return trend, plunge
import math
from ZeroTwoPi import ZeroTwoPi

east = math.pi/2

# def tp2sd(trd, plg) – maybe shorter name is a better one
def trend_plunge_to_strike_dip(trend, plunge):
  if plg >= 0:
    strike = east - plunge
    dip = ZeroTwoPi(trend + east)
  else: # Unusual case of pole pointing upwards
    strike = east + plunge
    dip = ZeroTwoPi(trend - east)
  return (strike, dip)

# def sd2tp(strike, dip)
def strike_dip_to_trend_plunge(strike, dip):
  plunge = east - dip;
  trend = ZeroTwoPi (strike - east)
  return (trend, plunge)
# Circulation.py - from gvcalc.f
import math


class Circulation(object):
    """calculate local circulation for blade slice"""

    def __init__(
        self,
        ctx,
        chord,  # local chord (inch)
        AoA,  # blade angle of attack (degrees)
        radius,  # local blade section chord
    ):
        self.nblades = ctx.nblades
        self.tip_radius = ctx.tip_radius
        self.v_inf = ctx.v_inf
        self.rpm = ctx.RPM * math.pi / 180.0

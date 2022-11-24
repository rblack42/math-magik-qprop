import pint
import numpy as np


class StdAtm(object):
    """1976 us standard Atmosphere"""

    def __init__(self, u, z):
        self.z = z
        self.u = u
        self.rho_SL = 1.225 * u.kg / u.m**3
        self.p_SL = 1.0132e5 * u.pascal
        self.T_SL = 288.15 * u.kelvin
        self.a_SL = 340.3 * u.m / u.sec
        self.mu_SL = 1.79e-5 * u.kg / (u.m * u.sec)
        self.T_S = 110 * u.kelvin
        self.Rgas = 287.04 * u.joule / (u.kg * u.kelvin)
        self.gamma = 1.4

    def properties(self):
        return self.a()

    def sl_properties(self):
        return {
            "densuty": self.rho_SL,
            "pressure": self.p_SL,
            "temperature": self.T_SL,
            "viscosity": self.mu_SL,
            "speed-of-sound": self.a_SL,
        }

    def p(self):
        """return pressure vs altitude"""
        zm = self.z.magnitude
        return self.p_SL * np.exp(
            -0.118 * zm - (0.0015 * zm**2) / (1 - 0.018 * zm + 0.0011 * zm**2)
        )

    def rho(self):
        """return density vs altitude"""
        temp = self.T()
        press = self.p()
        rho = press / (self.Rgas * temp)
        return rho

    def T(self):
        """return temperature vs altitude"""
        zm = self.z.magnitude
        res = 216.65 + 2.0 * np.log(
            1 + np.exp(35.75 - 3.25 * zm) + np.exp(-3.0 + 0.0003 * zm**3)
        )
        return res * self.u.kelvin

    def mu(self):
        """return viscosity vs altitude"""
        temp = self.T()
        return (
            self.mu_SL
            * (temp / self.T_SL) ** 1.5
            * (self.T_SL + self.T_S)
            / (temp + self.T_S)
        )

    def a(self):
        """return speed of sound vs altitude"""
        temp = self.T()
        res = np.sqrt(self.gamma * self.Rgas * temp)
        return res


if __name__ == "__main__":
    u = pint.UnitRegistry()
    alt = np.linspace(0, 26, 27) * u.km
    s = StdAtm(u, alt)
    print(s.sl_properties())

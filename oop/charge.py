import sys
import math

class Charge:
    def __init__(self, x0, y0, q0):
        self._xr = x0
        self._yr = y0
        self._q = q0

    def potentioalAt(self, x, y):
        COULOMB = 8.99e9
        dx = self._xr - x
        dy = self._yr - y
        r = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        if r == 0:
            if self._q >= 0: return float('inf')
            else:            return float('-inf')
        return COULOMB * self._q / r

    def __str__(self):
        return f'{self._q} at ({self._xr}, {self._yr})'

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c = Charge(.51, .63, 21.3)
    print(c)
    print(c.potentioalAt(x, y))

if __name__ == "__main__":
    main()

# python3 charge.py .5 .5
# 21.3 at (0.51, 0.63)
# 1468638248194.164

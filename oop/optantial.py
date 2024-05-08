from charge import Charge
from picture import Picture
from color import Color
import stdio, stddraw
import random

def readcharges():
    n = stdio.readInt()
    a = [None] * n
    for i in range(n):
        x0 = stdio.readFloat()
        y0 = stdio.readFloat()
        q0 = stdio.readFloat()
        a[i] = Charge(x0, y0, q0)
    return a

def toGray(v):
    v = 128 + v / 2.0e10
    if v >= 255: t = 255
    elif v <= 0: t = 0
    else: t = int(v)
    return Color(t, t, t)

def toColor(v):
    v = 128 + v / 2.0e10
    if v > 255: r, g, b = random.randint(0, 255), 0, 0
    elif v < 0: r, g, b = 0, 0, random.randint(0, 255)
    else       : r, g, b = 0, random.randint(0, 255),0
    return Color(r, g, b)

def main():
    SIZE = 512
    a = readcharges()
    pic = Picture(SIZE, SIZE)
    for col in range(SIZE):
        for row in range(SIZE):
            x = float(col/SIZE)
            y = float(row/SIZE)
            v = 0.0
            for c in a:
                v += c.potentioalAt(x, y)
            pic.set(col , SIZE-1-row, toColor(v))
    stddraw.setCanvasSize(SIZE, SIZE)
    stddraw.picture(pic)
    stddraw.show()

if __name__ == '__main__':
    main()

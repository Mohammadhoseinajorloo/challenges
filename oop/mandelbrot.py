import sys, stddraw
from picture import Picture
from complex import Complex
from color import Color

def mandel(z0, limit=255):
    z = z0
    for t in range(limit):
        if abs(z) >= 2.0: return t
        z = z * z + z0
    return limit


def main():
    MAX = 255
    n = int(sys.argv[1])
    xc = float(sys.argv[2])
    yc = float(sys.argv[3])
    size = float(sys.argv[4])
    pic = Picture(n, n)
    for col in range(n):
        for row in range(n):
            x0 = xc - (size/2)+(size*col/n)
            y0 = yc - (size/2)+(size*row/n)
            z0 = Complex(x0, y0)
            gray= MAX - mandel(z0, MAX)
            color = Color(gray, gray, gray)
            pic.set(col, n-1-row, color)
    stddraw.setCanvasSize(n, n)
    stddraw.picture(pic)
    stddraw.show()

if __name__ == "__main__":
    main()

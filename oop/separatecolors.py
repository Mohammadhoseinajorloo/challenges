import sys, stddraw
from picture import Picture
from color import Color 

filename = sys.argv[1]

source = Picture(filename)

w = source.width()
h = source.height()

R = Picture(w, h)
G = Picture(w, h)
B = Picture(w, h)

for col in range(w):
    for row in range(h):
        pixel = source.get(col, row)
        r = pixel.getRed()
        g = pixel.getGreen()
        b = pixel.getBlue()
        R.set(col, row, Color(r, 0, 0))
        G.set(col, row, Color(0, g, 0))
        B.set(col, row, Color(0, 0, b))

stddraw.setCanvasSize(w, h)
for i in [R, G, B]:
    stddraw.picture(i)
    stddraw.show(1000)



# 3.Modify alberssquares.py to take nine command-line arguments that specify three colors and then draws the six squares showing all the Albers squares with the large square in each color and the small square in each different color.
import sys
import stddraw
from color import Color

#-----------------------------------------------------------------------

# Accept integers r1, g1, b1, r2, g2, and b2 as command-line arguments.
# Draw to standard draw Albers squares using colors (r1, g1, b1) and
# (r2, g2, b2).

r1 = int(sys.argv[1])
g1 = int(sys.argv[2])
b1 = int(sys.argv[3])
c1 = Color(r1, g1, b1)

r2 = int(sys.argv[4])
g2 = int(sys.argv[5])
b2 = int(sys.argv[6])
c2 = Color(r2, g2, b2)

r3 = int(sys.argv[7])
g3 = int(sys.argv[8])
b3 = int(sys.argv[9])
c3 = Color(r3, g3, b3)

stddraw.setCanvasSize(512, 256)
stddraw.setYscale(.25, .75)

stddraw.setPenColor(c1)
stddraw.filledSquare(.25, .5, .2)

stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .5, .1)

stddraw.setPenColor(c3)
stddraw.filledSquare(.25, .5, .05)

stddraw.setPenColor(c3)
stddraw.filledSquare(.75, .5, .2)

stddraw.setPenColor(c2)
stddraw.filledSquare(.75, .5, .1)

stddraw.setPenColor(c1)
stddraw.filledSquare(.75, .5, .05)

stddraw.show()

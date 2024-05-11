import sys, stddraw, stdrandom
from turtle import Turtle

def main():
    stepcount = int(sys.argv[1])
    stepsize = float(sys.argv[2])

    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)

    turtle = Turtle(.5, .5, .0)

    for count in range(stepcount):
        turtle.turnLeft(stdrandom.uniformFloat(.0, 360.0))
        turtle.goForward(stepsize)
        stddraw.show(0.0)
    stddraw.show()
    
if __name__ == "__main__":
    main()

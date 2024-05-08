from turtle import Turtle
import sys, math, stddraw

def main():
    n = int(sys.argv[1])
    wraps = int(sys.argv[2])
    decay = float(sys.argv[3])

    angle = 360.0/n
    step = math.sin(math.radians(angle/2.0))
    turtle = Turtle(.5, .0, angle/2.0)

    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)

    for i in range(wraps * n):
        step /= decay 
        turtle.goForward(step)
        turtle.turnLeft(angle)
    stddraw.show()

if __name__ == "__main__":
    main()

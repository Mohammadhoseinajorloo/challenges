from turtle import Turtle
import sys, math, stddraw

def main():
    n = int(sys.argv[1])
    turtle = Turtle(.5, .0, 180.0/n)
    step = math.sin(math.radians(180.0/n))
    stddraw.clear(stddraw.LIGHT_GRAY)
    for i in range(n):
        turtle.goForward(step)
        turtle.turnLeft(360.0/n)
    stddraw.show()

if __name__ == "__main__":
    main()

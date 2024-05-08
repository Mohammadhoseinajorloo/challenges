import stddraw, sys
from turtle import Turtle

def koch(n , step_size, turtle):
    if n == 0:
        turtle.goForward(step_size)
        return
    koch(n -1 , step_size, turtle)
    turtle.turnLeft(60.0)
    koch(n-1, step_size, turtle)
    turtle.turnLeft(-120.0)
    koch(n-1, step_size, turtle)
    turtle.turnLeft(60)
    koch(n-1, step_size, turtle)

def main():
    n = int(sys.argv[1])

    w = 512
    h = 256
    stddraw.setCanvasSize(w, h)
    stddraw.setPenRadius(.0)
    stddraw.setYscale(-.1, .4)
    stddraw.clear(stddraw.LIGHT_GRAY)
    step_size = 1.0 / (3.0 ** n)
    turtle = Turtle(.0, .0, .0)
    koch(n, step_size, turtle)
    stddraw.show()

if __name__ == "__main__":
    main()

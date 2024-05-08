from turtle import Turtle
import stddraw

def main():

    turtle = Turtle(.0, .0, .0)

    turtle.goForward(1.0)
    turtle.turnLeft(120.0)
    turtle.goForward(1.0)
    turtle.turnLeft(120.0)
    turtle.goForward(1.0)
    turtle.turnLeft(120.0)

    stddraw.show()

if __name__ == "__main__":
    main()

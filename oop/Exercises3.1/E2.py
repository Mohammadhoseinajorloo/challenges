# 2.Compose a program that takes from the command line three integers between 0 and 255 that represent red, green, and blue values of a color and then creates and shows a 256-by-256 Picture of that color.
from picture import Picture
from color import Color
import sys, stddraw

def main():
    size = 256
    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])

    color = Color(red, green, blue)
    picture = Picture(size, size)

    for row in range(size):
        for col in range(size):
            picture.set(row, col, color)

    stddraw.setCanvasSize(size, size)
    stddraw.picture(picture)
    stddraw.show()


if __name__ == "__main__":
    main()

# 4.Compose a program that takes the name of a grayscale picture file as a command-line argument and uses stddraw to plot a histogram of the frequency of occurrence of each of the 256 grayscale intensities.
from picture import Picture
from color import Color
import sys, stddraw

def main():
    pic1 = Picture(sys.argv[1])
    h = pic1.height()
    w = pic1.weight()
    pic2 = Picture(h, w)

    for row in range(w):
        for col in range(h):
            


if __name__ == "__main__":
    main()

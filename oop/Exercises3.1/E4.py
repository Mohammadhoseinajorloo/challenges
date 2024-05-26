# 4.Compose a program that takes the name of a grayscale picture file as a command-line argument and uses stddraw to plot a histogram of the frequency of occurrence of each of the 256 grayscale intensities.
from picture import Picture
from color import Color
import sys, stddraw

def histogram(data, nbins, min_val=None, max_val=None):
    hist_vals = [0]*(nbins+1)
    if min_val is None:
        min_val = min(data)
    if max_val is None:
        max_val = max(data)

    for d in data:
        bin_number = int(nbins * ((d - min_val) / (max_val - min_val)))
        hist_vals[bin_number] += 1
    bin_lower_bounds = [min_val + i*(max_val - min_val)/len(hist_vals) for i in range(len(hist_vals))]
    return hist_vals, bin_lower_bounds

def main():
    pic1 = Picture(sys.argv[1])
    h = pic1.height()
    w = pic1.width()

    list_ = []
    for row in range(w):
        for col in range(h):
            b = pic1.get(row, col).getBlue()
            if b not in list_:
                list_.append(b)
    hist_vals = histogram(list_, 3)
    for i in hist_vals[0]:
        stddraw.setCanvasSize(512, 512)
        stddraw.setYscale(.5)
        stddraw.filledRectangle(1, 2, 1.0, i)
        stddraw.show()

if __name__ == "__main__":
    main()

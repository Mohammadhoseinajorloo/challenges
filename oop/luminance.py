from color import Color
import stdio

def luminance(color):
    red = color.getRed()
    green = color.getGreen()
    blue = color.getBlue()
    return int((.299 * red) + (.587 * green) + (.114 * blue))

def iscompatible(c1, c2):
    return abs((luminance(c1) - luminance(c2))) >= 128

def togray(c):
    y = int(round(luminance(c)))
    return Color(y, y, y)


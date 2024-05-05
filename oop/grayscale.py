import stddraw, sys, luminance
from picture import Picture

#pic = Picture(sys.argv[1])
#
#for col in range(pic.width()):
#    for row in range(pic.height()):
#        print(pic.height() - row - 1 )
#        pic.set(col, pic.height() - row -1, pic.get(col, row))
#        pic.set(col, row, pic.get(col, row))
#        pixel = pic.get(col, row)
#        gray = luminance.togray(pixel)
#        pic.set(col, row, gray)

source = Picture(sys.argv[1])
w = source.width()
h = source.height()
target = Picture(w, h)
for col in range(w):
    for row in range(h):
        target.set(w-col-1, row, source.get(col, row))
#        target.set(col, h - row - 1, source.get(col, row))

stddraw.setCanvasSize(target.width(), target.height())
stddraw.picture(target)
stddraw.show()

import sys
from instream import InStream

in0 = InStream(sys.argv[1])
in1 = InStream(sys.argv[2])

s = in0.readAll()
t = in1.readAll()

print(s == t)

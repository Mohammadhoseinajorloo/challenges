import sys
from instream import InStream
from outstream import OutStream

def cat_file():
    inFilename = sys.argv[1:-1]
    outFilename = sys.argv[-1]
    out = OutStream(outFilename)

    for filename in inFilename:
        in_ = InStream(filename)
        s = in_.readAll()
        out.write(s)

if __name__ == "__main__":
    cat_file()

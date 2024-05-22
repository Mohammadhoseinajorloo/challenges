# 1.Compose a program that takes a float command-line argument w, creates four Charge objects (each with charge value 1.0) that are each distance w in each of the four cardinal directions from (.5, .5), and writes the potential at (0.25, 0.5).
import sys
from charge import Charge

def main():
    w = float(sys.argv[1])
    cx = .5
    cy = .5

    px = .25
    py = .5

    ch1 = Charge(cx + w, cy, 1.0)
    ch2 = Charge(cx, cy + w, 1.0)
    ch3 = Charge(cx - w, cy, 1.0)
    ch4 = Charge(cx, cy - w, 1.0)

    v1 = ch1.potentialAt(px, py)
    v2 = ch2.potentialAt(px, py)
    v3 = ch3.potentialAt(px, py)
    v4 = ch4.potentialAt(px, py)

    total = v1 + v2 + v3 + v4
    print(f"total potential: {total}")

if __name__ == "__main__":
    main()
#-------------------------------------
# python3 E1.py 500000000
# total potential: 71.92
#-------------------------------------
# python3 E1.py 0.000005
# total potential: 143840000014.38397

import stdio
import sys

def ispotentialgene(dna):
    if (len(dna) % 3) != 0 : return False
    if not dna.startswith('ATG'): return False
    for i in range(len(dna) - 3):
        if dna[i:i+3] == "TAG" : return False
        if dna[i:i+3] == "TAA" : return False
        if dna[i:i+3] == "TGA" : return False
    if dna.endswith("TAG") or dna.endwith("TAA") or dna.endwith("TGA") : return True
    return False

if __name__ == "__main__":
    dna = sys.argv[1]
    bl = ispotentialgene(dna)
    stdio.writeln(bl)

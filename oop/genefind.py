import stdio
import sys

def findgene():
    start = sys.argv[1]
    stop = sys.argv[2]
    genome = stdio.readAll()
    beg = -1
    for i in range(len(genome)-2):
        codon = genome[i:i+3]
        if codon == start: beg = i
        if codon == stop and beg != -1:
            gene = genome[beg+3:i]
            if len(gene) % 3 == 0:
                stdio.writeln(gene)
                beg = -1

if __name__ == "__main__":
    findgene()

##############################################
# python3 genefind.py ATG TAG < genometiny.txt
# CATAGCGCA
# TGC
##############################################

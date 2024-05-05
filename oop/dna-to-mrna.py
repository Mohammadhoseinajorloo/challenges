import stdio

def translate(dna):
    dna = dna.upper()
    dna = dna.replace("T", "U")
    return dna

if __name__ == "__main__":
    dna = "ATGCGGTACTTA"
    dna = translate(dna)
    stdio.writeln(dna)

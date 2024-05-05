import stdio

def issorted(lis):
    for i in range(1, len(lis)):
        if lis[i] < lis[i-1]:
            return False
    return True

if __name__ == "__main__":
    lis = [1,2,3,4,5,6,7]
    lis2 = [1,4,3,2,7,5,6]
    check = issorted(lis)
    check2 = issorted(lis2)
    stdio.writeln(check)
    stdio.writeln(check2)

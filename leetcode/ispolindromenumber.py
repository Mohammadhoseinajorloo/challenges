

def ispolidrome(x:int) -> bool:
    x = str(x)
    for c in range(len(x)):
        if x[c] != x[len(x)-c-1]:
            return False
    return True

def isPolindrome(x:int) -> bool:
    x = str(x)
    if x[::-1] != x:
        return False
    return True

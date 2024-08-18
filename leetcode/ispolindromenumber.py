
def isPalindrome3(x: int) -> bool:
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x

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

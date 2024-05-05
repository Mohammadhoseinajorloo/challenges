import stdio

def ispalindrome(s):
    s = s.lower()
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True

def ispolindrome2(word):
    word = word.lower()
    counter = -1
    for letter in word:
        if letter != word[counter]:
            return False
        return True

if __name__ == "__main__":
    s = input('please enter word: ')
    s1 = ispalindrome(s)
    s2 = ispolindrome2(s)
    stdio.writeln(s1)
    stdio.writeln(s2)

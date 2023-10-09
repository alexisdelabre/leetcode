def isPalindrome(x: int) -> bool:
    toStr = str(x)
    lenght = len(toStr)

    if x > 0:
        for i in range(int(lenght/2)):
            if toStr[i] == toStr[-(i+1)]:
                continue
            else:
                return False
        return True
    return False

print(isPalindrome(121))
print(isPalindrome(12321))
print(isPalindrome(12345))
print(isPalindrome(-121))
print(isPalindrome(10))
def isPalindrome(s: str) -> bool:

    # Remove punctuation and convert to lowercase
    # cleaned_s = ''.join([c.lower() for c in s if c.isalnum()])
    # print(cleaned_s)

    # c = cleaned_s.replace(" ", "")

    # return True if c == c[::-1] else False

    for i in range(0, 10, 2):
        print(i)

isPalindrome("A man, a plan, a canal: Panama")
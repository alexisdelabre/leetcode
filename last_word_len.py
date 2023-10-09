def lengthOfLastWord(s: str) -> int:

    print (s.strip())
    previousWasSpace = True
    countRemoved = 0
    for index, char in enumerate(s):
        index -= countRemoved
        print(index, s[index])
        if s[index] == ' ':
            if previousWasSpace or index == len(s):
                print('to remove')
                s = s[:index] + s[index+1:]
                countRemoved+=1
            previousWasSpace = True
        else:
            previousWasSpace = False
    if s[-1] == ' ':
        s = s[:-1]

    return len(s.split(' ')[-1])


print(lengthOfLastWord('   fly me   to   the moon  '))
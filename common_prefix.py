def longestCommonPrefix(strs) -> str:
    # Find the length of the shortest word
    min_length = min(len(word) for word in strs)
    
    prefix = ''
    # Iterate over the characters up to the length of the shortest word
    for i in range(min_length):
        char = []
        for word in strs:
            char.append(word[i])

        if len(set(char)) != 1:
            return prefix
        prefix += list(set(char))[0]
        

    return prefix
    
longestCommonPrefix(["flower", "flow", "flight"])
def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1

    for i in range(len(haystack)- len(needle) + 1):
        print(i)
        print(haystack[i:i+len(needle)])
        if haystack[i:i+len(needle)] == needle:
            print(i)
            return i



strStr('sadbutsad', 'sad')
def strStr(self, haystack: str, needle: str) -> int:
    if needle == "": return 0
    length = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+length] == needle:
            return i
    
    return -1


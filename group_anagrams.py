def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = {}
    for string in strs:
        s = ''.join(sorted(string))
        if s in anagrams:
            anagrams[s].append(string)
        else:
            anagrams[s] = [string]
    
    return anagrams.values()

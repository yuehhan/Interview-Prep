<<<<<<< HEAD
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = {}
    for string in strs:
        s = ''.join(sorted(string))
        if s in anagrams:
            anagrams[s].append(string)
        else:
            anagrams[s] = [string]
    
    return anagrams.values()
=======
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = {}
    for string in strs:
        s = ''.join(sorted(string))
        if s in anagrams:
            anagrams[s].append(string)
        else:
            anagrams[s] = [string]
    
    return anagrams.values()
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef

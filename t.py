class Solution:
    def is_permutation(s1: str, s2: str):
        for i in range(len(s1)):
        chars[s1[i]] = i

        print(chars)
        for i in range(len(s2)):
            if s2[i] not in chars:
                return False
        return True
    
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        for i in range(len(s1)):
            s1_chars[s1[i]] = i
        
        substr_start = 0
        
        for i in range(len(s2)):
            if s2[i] in s1_chars:
                pass
            else:
                substr_start = i
            if i - substr_start == len(s1):
                return True
        return False
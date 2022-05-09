# longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charsSet = set()
        left, right = 0, 0
        result = 0

        while right < len(s):
            while s[right] in charsSet:
                charsSet.remove(s[left])
                left += 1
            charsSet.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        return result


t = Solution()
input = "pwwkew"
print(input)
print(t.lengthOfLongestSubstring(input))
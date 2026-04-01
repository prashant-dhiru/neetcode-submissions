class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0] * 26
        for char in s:
            char_index = ord('a') - ord(char)
            seen[char_index] += 1
        for char in t:
            char_index = ord('a') - ord(char)
            seen[char_index] -= 1
                 
        for count in seen:
            if not count == 0: return False  
        return True


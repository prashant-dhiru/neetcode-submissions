class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count = defaultdict(int)
        for char in s:
            word_count[char] = word_count[char] + 1
        for char in t:
            word_count[char] = word_count[char] - 1
        for char,count in word_count.items():
            if count != 0:
                print(char)
                return False
        return True
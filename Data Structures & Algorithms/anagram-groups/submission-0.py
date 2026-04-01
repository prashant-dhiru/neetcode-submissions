class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list) #char_count_hash : list_of_words
        for s in strs:
            char_count = [0] * 26
            for char in s:
                char_count[ord(char)-ord('a')] += 1
            anagram_dict[tuple(char_count)].append(s)
        return list(anagram_dict.values())
        
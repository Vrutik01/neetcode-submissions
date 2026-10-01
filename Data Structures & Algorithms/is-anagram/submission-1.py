class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        for char in t:
            if char not in freq:
                return False

            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]

        return freq == {}
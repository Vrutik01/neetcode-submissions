class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def mapValues(word: str) -> List[int]:
            chars = [0] * 26

            for w in word:
                index = ord(w) - ord('a')
                chars[index] += 1
            
            return tuple(chars)

        groupWords = {}

        for word in strs:
            group = mapValues(word)
            if group not in groupWords:
                groupWords[group] = []

            groupWords[group].append(word)
        
        return list(groupWords.values())
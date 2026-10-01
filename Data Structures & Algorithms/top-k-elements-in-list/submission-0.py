class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        maxFreq = -1

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            maxFreq = max(maxFreq, freq[n])

        kItems = [[] for _ in range(maxFreq)]

        for key, val in freq.items():
            kItems[val - 1].append(key)

        res = []
        for i in range(maxFreq - 1, - 1, -1):
            for item in kItems[i]:
                res.append(item)
                if len(res) == k:
                    return res

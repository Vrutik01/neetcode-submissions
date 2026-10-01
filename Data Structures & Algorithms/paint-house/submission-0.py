class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def findMinCost(house: int, skipColor: int):
            if house >= len(costs):
                return 0

            if (house, skipColor) in dp:
                return dp[(house, skipColor)]

            dp[(house, skipColor)] = float("inf")
            for i in range(3):
                if i == skipColor:
                    continue

                dp[(house, skipColor)] = min(
                    dp[(house, skipColor)],
                    costs[house][i] + findMinCost(house + 1, i)
                )

            return dp[(house, skipColor)]

        dp = {}
        return findMinCost(0, -1)
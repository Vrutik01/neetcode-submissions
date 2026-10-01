class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp stores the cumulative minimum cost for the previous house
        # initialized with the costs of the first house
        dp = [0, 0, 0]
        
        for c0, c1, c2 in costs:
            # Calculate current house costs based on previous house's best options
            # We use temporary variables (or tuple unpacking) to avoid overwriting 
            # values we still need for the current iteration.
            dp = [
                c0 + min(dp[1], dp[2]),
                c1 + min(dp[0], dp[2]),
                c2 + min(dp[0], dp[1])
            ]
            
        return min(dp)
        # dp = [[float("inf")] * 3 for _ in range(len(costs) + 1)]

        # for i in range(3):
        #     dp[len(costs)][i] = 0

        # for house in range(len(costs) - 1, -1, -1):
        #     dp[house][0] = min(
        #         dp[house][0],
        #         costs[house][0] + min(dp[house + 1][1], dp[house + 1][2])
        #     )
        #     dp[house][1] = min(
        #         dp[house][1],
        #         costs[house][1] + min(dp[house + 1][0], dp[house + 1][2])
        #     )
        #     dp[house][2] = min(
        #         dp[house][2],
        #         costs[house][2] + min(dp[house + 1][0], dp[house + 1][1])
        #     )

        # return min(dp[0][0], dp[0][1], dp[0][2])


        # def findMinCost(house: int, skipColor: int):
        #     if house >= len(costs):
        #         return 0

        #     if (house, skipColor) in dp:
        #         return dp[(house, skipColor)]

        #     dp[(house, skipColor)] = float("inf")
        #     for i in range(3):
        #         if i == skipColor:
        #             continue

        #         dp[(house, skipColor)] = min(
        #             dp[(house, skipColor)],
        #             costs[house][i] + findMinCost(house + 1, i)
        #         )

        #     return dp[(house, skipColor)]

        # dp = {}
        # return findMinCost(0, -1)
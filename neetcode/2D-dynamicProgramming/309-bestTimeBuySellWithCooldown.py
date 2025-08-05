class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = dict()
        def dfs(i, price):
            if (i, price) in dp:
                return dp[(i, price)]

            if i >= len(prices):
                return 0

            res = 0
            notHolding = price < 0
            if notHolding: 
                # can either buy or skip
                res = max(dfs(i + 1, prices[i]), dfs(i + 1, price))
            else:
                # can either sell or skip
                res = max(prices[i] - price + dfs(i + 2, -1), dfs(i + 1, price))

            dp[(i, price)] = res
            return res

        return dfs(0, -1)
        

    def maxProfit2(self, prices: List[int]) -> int:

        def dfs(i, price):
            if i >= len(prices):
                return 0

            notHolding = price < 0
            if notHolding: 
                # can either buy or skip
                return max(dfs(i + 1, prices[i]), dfs(i + 1, price))
            else:
                # can either sell or skip
                return max(prices[i] - price + dfs(i + 2, -1), dfs(i + 1, price))

        return dfs(0, -1)
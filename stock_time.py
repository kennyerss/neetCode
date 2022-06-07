class Solution:
    def max_profit(self, prices: List[int]) -> int:
        curr_max = 0  # Tracks profit
        # Two pointers, left and right days
        day1 = 0
        day2 = 1
        while day2 < len(prices):
            # If profitable
            if prices[day1] < prices[day2]:
                profit = prices[day2] - prices[day1]
                curr_max = max(curr_max, profit)  # Updates max profit
            else:
                day1 = day2  # Otherwise makes day1 ptr to day2 ptr

                day2 += 1  # Updates day2 pointer to the right

        return curr_max

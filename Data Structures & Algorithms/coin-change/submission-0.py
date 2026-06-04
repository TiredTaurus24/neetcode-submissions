class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = [0] + [float('inf')] * (amount)
  
        for j in range(1, amount + 1):
            for i in coins:
                if i <= j:
                    c[j] =  min(c[j], 1 + c[j-i])
        return c[amount] if c[amount] != float('inf') else -1


        
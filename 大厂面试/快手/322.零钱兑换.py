"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def coin_change(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float('inf') for c in coins) + 1
        return dp[-1] if dp[-1] != float('inf') else -1

    @staticmethod
    def coin_change2(coins, amount):
        if not amount:
            return 0
        if not coins:
            return -1
        if len(coins) == 1 and coins[0] > amount:
            return -1
        mem = [-1] * (amount + 1)
        mem[0] = 0
        for i in range(1, amount + 1):
            cur_min = amount + 1
            for c in coins:
                if c <= i:
                    cur_min = mem[i - c] if mem[i - c] < cur_min else cur_min
                mem[i] = cur_min + 1 if cur_min < amount + 1 else amount + 1
        if mem[-1] == amount + 1:
            return -1
        else:
            return mem[-1]


if __name__ == '__main__':
    coins = [1, 2, 5]
    coins2 = [1, 3, 4]
    amount = 11
    amount2 = 6
    coins3 = [1]
    amount3 = 0
    print(Solution().coin_change(coins, amount))
    print(Solution().coin_change(coins2, amount2))
    print(Solution().coin_change(coins3, amount3))

    print(Solution().coin_change2(coins, amount))
    print(Solution().coin_change2(coins2, amount2))
    print(Solution().coin_change2(coins3, amount3))

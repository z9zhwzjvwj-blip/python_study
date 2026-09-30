n1 = 1
n2 = 2
n3 = 3


def climbStairs(n):
    memo = {}

    def dp(x):
        if x == 1:
            return 1
        elif x == 2:
            return 2
        else:
            if x in memo:
                return memo[x]

        memo[x] = dp(x - 1) + dp(x - 2)
        return memo[x]

    return dp(n)


print(climbStairs(3))

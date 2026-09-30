prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    minimum = prices[0]
    max_profit = 0

    for price in prices:
        minimum = min(price, minimum)
        max_profit = max(price - minimum, max_profit)

    return max_profit


print(maxProfit(prices))

def max_profit(prices):
    max_profit = 0
    buy = 0

    for sell in range(0, len(prices)):
        if prices[sell] < prices[buy]:
            buy = sell
        else:
            max_profit += prices[sell] - prices[buy]
            buy = sell

    return max_profit

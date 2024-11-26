def maxProfit(prices):
    max_profit = 0
    buy = 0

    for sell in range(0, len(prices)):
        if prices[sell] < prices[buy]:
            buy = sell
            continue

        profit = prices[sell] - prices[buy]
        if profit > max_profit:
            max_profit = profit

    return max_profit

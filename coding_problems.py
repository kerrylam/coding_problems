# def one_away(word1, word2):
#     difference = 0
#     i = 0
#     while i < len(word1):
#         if word1[i] != word2[i]:
#             difference += 1
#             i += 1
#     return difference <= 1

def get_max_profit(stock_prices):
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]
    for price in stock_prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price
    return max_profit
    






def buy_and_sell_stock(prices):
  min_price_so_far, maxprofit = float('inf'), 0.0
  for price in prices:
    max_profit_sell_today = price - min_price_so_far
    max_profit = max(max_profit, max_profit_sell_today)
    min = min(min_price_so_far, price)
  
  return max_profit

print(buy_and_sell_stock([310,310,275,275,260,260,260,230,230,230]))


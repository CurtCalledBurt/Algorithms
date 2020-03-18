#!/usr/bin/python

import argparse

test_array = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  if len(prices) <= 1:
    return float("-inf")
  
  max_profit = find_max_profit(prices[1:])

  for i in range(1, len(prices)):
    if prices[i] - prices[0] > max_profit:
      max_profit = prices[i] - prices[0]
  
  return max_profit

print(find_max_profit(test_array))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
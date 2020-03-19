#!/usr/bin/python

import sys

coins = [1, 5, 10, 25, 50]

def eating_cookies(n, cache={0: 1}):
    ways_eat_cookies = 0
    if n in cache:
      return cache[n]

    for num_eat_cookies in [1, 2, 3]:
      if n - num_eat_cookies >= 0:
        ways_eat_cookies += eating_cookies(n - num_eat_cookies)
        cache[n] = ways_eat_cookies

    return cache[n]


# def make_change(amount, denominations):
#     change_combos = 0
#     if amount = 0:
#         return 1
    
#     change_array = [0] * len(denominations)
    
#     for c_index in range(len(denominations)):
#         if amount - denominations[c_index] >= 0:
#           change_array[c_index] += 1
  

def making_change(goal, coins):
    wallets = [[coin] for coin in coins]
    new_wallets = []
    collected = []

    for wallet in wallets:
        if sum(wallet) == goal:
            collected.append(wallet)

    while wallets:
        for wallet in wallets:
            summ = sum(wallet)
            for coin in coins:
                if coin >= wallet[-1]:
                    if summ + coin < goal:
                        new_wallets.append(wallet + [coin])
                    elif summ + coin == goal:
                        collected.append(wallet + [coin])
        wallets = new_wallets
        new_wallets = []
    return len(collected)

print(making_change(300, coins))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# Next steps: work on implementing cache, any input around 50 or over causes a slow down so bad 
# that the code never termininates before running out of memory.
# function is tested accurate up to n_cookies = 10

def eating_cookies(n, cache=None):
    ways_eat_cookies = 0
    if n == 0:
      return 1

    for num_eat_cookies in [1, 2, 3]:
      if n - num_eat_cookies >= 0:
        ways_eat_cookies += eating_cookies(n - num_eat_cookies)
    return ways_eat_cookies


print(eating_cookies( 50 ))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
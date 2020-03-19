#!/usr/bin/python

import sys

def construct_game(n):
  game = []
  if n == 0:
    return game

  game.append('play')
  game.extend(construct_game(n-1))

  return game

def rock_paper_scissors(n):
  games = []
  games.append(construct_game(n))
  # rock_paper_scissors(n)
  return games

print(rock_paper_scissors(3))





# s is a list
def rps(s):
   if len(s) == 1:
     return [s]

   perm_list = [] # resulting list
   for a in s:
     remaining_elements = [x for x in s if x != a]
     z = rps(remaining_elements) # permutations of sublist

     for t in z:
       perm_list.append([a] + t)

   return perm_list





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
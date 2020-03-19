#!/usr/bin/python

import sys

sys.setrecursionlimit(10**5)

def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    all_games = []

    def create_game(round, round_num):
        for i in range(len(options)):
          round.append(options[i])
          if round_num == n:
            all_games.append(round.copy())
          else:
            create_game(round, round_num + 1)
          round.pop()
    
    create_game([], 1)
    return all_games

print(rock_paper_scissors(5))


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
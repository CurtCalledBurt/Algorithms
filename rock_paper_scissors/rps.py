#!/usr/bin/python

import sys

def construct_games(n):
  pass

def rock_paper_scissors(n):
  plays = []
  if n == 0:
    return plays
  
  for play in ['rock', 'paper', 'scissors']:
    
    plays.append(play)
    plays.extend(rock_paper_scissors(n-1))
  return plays

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
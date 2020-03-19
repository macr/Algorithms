#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    hands = ['rock', 'paper', 'scissors']
    val = []
    for i in range(3**n):
        val.append([hands[i // 3**(n-1-j) % 3] for j in range(n)])
    return val


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

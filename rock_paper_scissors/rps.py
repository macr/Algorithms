#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    hands = ['rock', 'paper', 'scissors']
    base = len(hands)
    val = []
    for i in range(base**n):
        val.append([hands[i // base**(n-1-j) % base] for j in range(n)])
    return val


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

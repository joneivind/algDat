#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def mergeSort(decks):

    if len(decks) < 2:
        return decks

    mid = int(len(decks) / 2)

    L = mergeSort(decks[:mid])
    R = mergeSort(decks[mid:])

    return merge(L, R)


def merge(left, right):

    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.extend(deck)
    # Merge the decks and print result.

    solution = []

    for n, l in mergeSort(decks):
        solution.append(l)

    print (''.join(solution))


if __name__ == "__main__":
    main()
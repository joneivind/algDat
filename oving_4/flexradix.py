#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d):
    for i in range(d, 0, -1):
        A = countingSort(A, i)
    return A

def countingSort(aList, n):

    # A storage
    A = [None] * len(aList)

    # run through list and check if valid elements
    i = 0
    for words in aList:
        try:
            A[i] = aList[i][n-1] # get valid elements
        except(TypeError, IndexError):
            A[i] = 'a' # insert 'zero' elsewhere
        i += 1

    # min and max value of list
    minChar = ord('a')
    maxChar = ord('z')

    k = maxChar - minChar + 1

    B = [None] * len(A) # create a B list
    C = [0] * (k + 1) # create empty buckets

    # check how many times each letter appears in A pr iteration and add to C
    for j in range(0,len(A),1):
        C[ord(A[j][0]) - minChar] += 1

    for i in range(0,k):
        C[i] += C[i-1]

    for j in range(len(A)-1, -1, -1):
        B[C[ord(A[j][0]) - minChar] - 1] = aList[j]
        C[ord(A[j][0]) - minChar] -= 1

    return B


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()

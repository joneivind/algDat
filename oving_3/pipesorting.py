#!/usr/bin/python3

from sys import stdin
import math


def sort_list(A): # quicksort
    if len(A) <= 1:
        return A
    else:
        return sort_list([x for x in A[1:] if x < A[0]]) + [A[0]] + sort_list([x for x in A[1:] if x >= A[0]])


def binary_search(A, T): # binary search
    n = len(A)
    L = 0
    R = n - 1
    m = 0

    while L <= R:
        m = math.floor((L + R) / 2)
        if A[m] == T:
            break
        elif A[m] < T:
            L = m + 1
        else:
            R = m - 1

    return m


def find(A, lower, upper):
    A_lowest_index = binary_search(A, lower)
    A_highest_index = binary_search(A, upper)

    if lower < A[A_lowest_index] and A_lowest_index-1 != 0:
        A_lowest_index -= 1
    if upper > A[A_highest_index] and A_highest_index != len(A)-1:
        A_highest_index +=1

    return [A[A_lowest_index], A[A_highest_index]]



def main():
    input_list = []

    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
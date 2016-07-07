__author__ = 'MFO'

# Find the start of the biggest block in the array having ascending order

def solution(A):

    max_size_start = 0
    max_size = 1
    i = 0

    while i < len(A):

        start = i
        size = 1

        while i < len(A) and A[i] > A[i-1]:
            i += 1
            size += 1

        if size > max_size:
            max_size_start = start - 1
            max_size = size

        i += 1

    return max_size_start

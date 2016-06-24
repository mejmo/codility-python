__author__ = 'MFO'

def solution(A):
    max_slice = max_ending = 0

    for i in xrange(1, len(A)):
        max_ending = max(0, max_ending+A[i]-A[i-1])
        max_slice = max(max_slice, max_ending)
    return max_slice
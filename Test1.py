__author__ = 'MFO'

def solution(X, A):

    L = []

    for i in xrange(0, len(A)):
        if i == 0:
            if A[i] == X:
                L.append(1)
            else:
                L.append(-1)
        else:
            if A[i] == X:
                L.append(L[i-1]+1)
            else:
                L.append(L[i-1]-1)

    return L.index(0)+1 if 0 in L else 0


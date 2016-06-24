__author__ = 'MFO'

def make(A):
    s = 0
    for i in xrange(0, len(A)):
        s += A[i]*pow(-2, i)
    return s

def solution(A):

    s = make(A)

    res = -s
    bin = []

    while res != 0:
        rem = res % -2
        res = res / -2
        if rem < 0:
            rem += 2
            res += 1
        bin.append(rem)

    print "Before: "+str(make(A))+" Then: "+str(make(bin))

    return bin

print solution([1])





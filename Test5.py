from sre_parse import isdigit

# Compare two texts which are read from OCR devices and unrecognized chars are replaced with numbers which represents
# occurences count of the unrecognized characters.

__author__ = 'MFO'

def solution(S, T):

    return True if compare(normalize(S), normalize(T)) else False

def normalize(S):

    normalized = ''
    i = 0

    while i < len(S):

        if isdigit(S[i]) and int(S[i]) > 0:
            num = ''
            while i != len(S) and isdigit(S[i]):
                num += str(S[i])
                i += 1
            for j in xrange(0, int(num)):
                normalized += '#'
        else:
            normalized += S[i]
            i += 1

    return normalized

def compare(S, T):

    if len(S) != len(T):
        return False

    for i in xrange(0, len(S)):
        if S[i] != '#' and T[i] != '#' and S[i] != T[i]:
            return False

    return True

__author__ = 'MFO'

def make_move(X, Y, A, B, old_pos, moves, found=[]):

    # if len(pos_moves) == 0:
    #     return

    x = moves.pop()
    old_pos.append([X, Y])

    if ([X+x[0], Y+x[1]] in old_pos):
        return

    X = X+x[0]
    Y = Y+x[1]

    if len(old_pos) > 100000000:
        return -2

    if (X == A and Y == B):
        found.append(len(old_pos))
    else:
        for move in moves:
            make_move(X, Y, A, B, old_pos, moves)


def solution(A, B):
    # write your code in Python 2.7
    X = 0
    Y = 0
    old_pos = []
    found = []

    moves = [[-3, +2], [-2, +3], [+2, +3], [+3, +2], [+3, -2], [+2, -3], [-2, -3], [-3, -2]]

    make_move(X, Y, A, B, old_pos, moves, found)
    return min(found)

print solution(4, 5)
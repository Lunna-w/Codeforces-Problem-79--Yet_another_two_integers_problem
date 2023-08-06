def min_moves(a, b):
    diff = abs(b - a)
    moves = diff // 10
    if diff % 10 != 0:
        moves += 1
    return moves

t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    print(min_moves(a, b))
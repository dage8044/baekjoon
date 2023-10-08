import sys
def input() : return sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)
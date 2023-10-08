import sys
input = sys.stdin.readline
from collections import defaultdict

N, P, Q, X, Y = map(int, input().rstrip().split())
arr = defaultdict(int)
arr[0] = 1

def dp(N):
    if arr[N] != 0:
        return arr[N]
    elif N <= 0:
        arr[N] = 1
        return arr[N]
    else:
        arr[N] = dp((N//Q)-X) + dp((N//P)-Y)
        return arr[N]
print(dp(N))
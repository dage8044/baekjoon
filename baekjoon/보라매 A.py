import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
hap = [False] * n
army = list(map(int, input().rstrip().split()))
happy = True

if sum(army) % x == 0: print(1)
else: print(0)
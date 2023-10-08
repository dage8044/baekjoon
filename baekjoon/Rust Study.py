import sys
input = sys.stdin.readline

N = int(input().rstrip())
plan = list(map(int, input().rstrip().split()))
study = list(map(int, input().rstrip().split()))
cnt = 0

for i in range(N):
    if study[i] >= plan[i]:
        cnt += 1

print(cnt)
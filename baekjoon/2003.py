import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

start, end = 0, 1
cnt = 0

while end <= N and start <= end:
    total = sum(nums[start:end])
    if total == M:
        cnt += 1
        end += 1
    elif total < M:
        end += 1
    else:
        start += 1

print(cnt)
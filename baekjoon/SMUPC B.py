import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
seat = []
for i in range(N):
    seat.append(input().rstrip())

cnt = 0
for i in range(N):
    for j in range(M-K+1):
        temp = seat[i][j:K+j]
        if temp == '0'*K:
            cnt += 1

print(cnt)
import sys
input = sys.stdin.readline
from collections import deque

def dfs(N):
    queue = deque()
    cnt = 0
    queue.append((N, cnt))
    while queue:
        x, time = queue.popleft()
        if x == K:
            return time
        if x < 0 or x > 100000:
            pass
        else:
            if not visited[x]:
                visited[x] = True
                queue.append((x-1, time+1))
                queue.append((x+1, time+1))
                queue.append((x*2, time+1))


N, K = map(int, input().rstrip().split())
visited = [False] * (200000)
print(dfs(N))
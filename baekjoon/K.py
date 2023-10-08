import sys
def input() : return sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
q = deque(enumerate(map(int,input().split())))
result=[]

while q:
    idx,num = q.popleft()
    result.append(idx+1)

    if num>0:
        q.rotate(-(num-1))

    elif num<0:
        q.rotate(-num)

print(*result)
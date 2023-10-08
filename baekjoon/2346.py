import sys
def input() : return sys.stdin.readline().rstrip()

n = int(input())
q = list(enumerate(map(int,input().split())))
result=[]
cursor = 0
while q:
    idx,num = q.pop(cursor)
    result.append(idx+1)
    cursor += num
    if q:
        if cursor >= len(q) or cursor <= -len(q):
            cursor %= len(q)
    
print(*result)
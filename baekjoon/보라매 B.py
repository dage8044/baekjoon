import sys
input = sys.stdin.readline

n, m, p= map(int, input().rstrip().split())
bunker = []
result = True
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    temp = sorted(temp)
    bunker.append(temp)

for i in range(n):
    items = 0
    if result:
        for j in range(m):
            if bunker[i][j] == -1:
                items += 1
            else:
                if bunker[i][j] <= p:
                    p += bunker[i][j]
                else:
                    while items > 0:
                        items -= 1
                        p *= 2
                        if p >= bunker[i][j]:
                            p += bunker[i][j]
                            break
                    if p < bunker[i][j]:
                        result = False
                        break
        if items != 0:
            for _ in range(items):
                p *= 2
    else:
        break
if result: print(1)
else: print(0)
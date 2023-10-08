import sys
def input() : return sys.stdin.readline().rstrip()

N = int(input())
classroom = []
one = False
two = False
for i in range(N):
    classroom.append(list(map(int, input().split())))
    for j in range(N):
        if classroom[i][j] == 2:
            student = (i, j)
        elif classroom[i][j] == 5:
            professor = (i, j)
x1, y1 = student
x2, y2 = professor
distance = abs(x1-x2) ** 2 + abs(y1-y2) ** 2
if distance >= 25:
    one = True

cnt = 0
x_min,x_max = min(x1,x2),max(x1,x2)
y_min,y_max = min(y1,y2),max(y1,y2)
for y in range(y_min,y_max+1):
    for x in range(x_min,x_max+1):
        if classroom[x][y] == 1:
            cnt += 1
if cnt >= 3:
    two = True
if one and two:
    print(1)
else:
    print(0)
import sys
input = sys.stdin.readline

freq = list(map(int, input().rstrip().split()))
nova = list(map(int, input().rstrip().split()))
origin = list(map(int, input().rstrip().split()))
nova_cnt, origin_cnt = 1, 1

nova.sort()
origin.sort()

temp = nova[0]
for i in range(1, len(nova)):
    cooltime = nova[i] - temp
    if cooltime >= 100:
        nova_cnt += 1
        temp = nova[i]

temp = origin[0]
for i in range(1, len(origin)):
    cooltime = origin[i] - temp
    if cooltime >= 360:
        origin_cnt += 1
        temp = origin[i]

print(nova_cnt, origin_cnt)
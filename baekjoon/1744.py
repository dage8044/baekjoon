import heapq
import sys
input=sys.stdin.readline

n = int(input())
arr=[]
plus = []
minus = []
result = 0

for i in range(n):
    arr.append(int(input().rstrip()))

heapq.heapify(arr)
while arr:
    temp = heapq.heappop(arr)
    if temp <= 0:
        minus.append(temp)
    else:
        plus.append(temp)
len_minus = len(minus)
len_plus = len(plus)
if len_minus != 0:
    if len_minus % 2 == 0:
        while minus:
            temp1 = minus.pop()
            temp2 = minus.pop()
            result += temp1 * temp2
    else:
        temp_minus = minus.pop()
        while minus:
            temp1 = minus.pop()
            temp2 = minus.pop()
            result += temp1 * temp2
        result += temp_minus
if len_plus != 0:
    if len_plus % 2 == 0:
        while plus:
            temp1 = plus.pop()
            temp2 = plus.pop()
            result += max(temp1 * temp2, temp1+temp2)
    else:
        while plus:
            if len(plus) == 1:
                result += plus.pop()
                break
            temp1 = plus.pop()
            temp2 = plus.pop()
            result += max(temp1 * temp2, temp1+temp2)
print(result)
    
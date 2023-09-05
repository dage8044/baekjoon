n = int(input().rstrip())
cnt = 0

for i in range(1, n+1):
    if i < 100:
        cnt += 1
    else:
        allow = True
        num = str(i)
        tolerance = (int(num[0]) - int(num[1]))  
        for j in range(1, len(num)-1):
            temp = (int(num[j]) - int(num[j+1]))
            if tolerance != temp:
                allow = False
                break
        if allow:
            cnt += 1
print(cnt)
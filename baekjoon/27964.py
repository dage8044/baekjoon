import sys
input = sys.stdin.readline  

n = int(input().rstrip())
result = set()
arr = list(input().rstrip().split())
for i in arr:
    if len(i) >= 6:
        if i[-6:] == 'Cheese':
            result.add(i)

if len(result) >= 4:
    print('yummy')
else: print('sad')
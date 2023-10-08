import sys
input = sys.stdin.readline  

N, M = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

for i in range(1, M):
    A[i] += A[i - 1]

for _ in range(N):
    B = int(input().rstrip())

    left, right = 0, M

    while right - left > 1:
        mid = (left + right) // 2

        if A[mid] <= B:
            left = mid
        
        else:
            right = mid
    
    if A[-1] < B:
        print('Go away!')
    
    elif B <= A[left]:
        print(left + 1)
    
    else:
        print(right + 1)
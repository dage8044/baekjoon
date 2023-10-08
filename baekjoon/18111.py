import sys
input = sys.stdin.readline  
from collections import Counter

N,M,B = map(int, input().rstrip().split())
mountain = []
hight = Counter()

for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    mountain.append(temp)
    hight += Counter(temp)


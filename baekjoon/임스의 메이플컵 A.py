import sys
input = sys.stdin.readline

spec = list(map(int, input().rstrip().split()))
one = False
two = False

if spec[0] >= 1000:
    one = True
if spec[1] >= 8000 or spec[2] >= 260:
    two = True

if one and two:
    print("Very Good")
elif one and not two:
    print("Good")
else:
    print("Bad")
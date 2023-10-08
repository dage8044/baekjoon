import sys
input = sys.stdin.readline

N = int(input().rstrip())
word = "WelcomeToSMUPC"
num = (N-1) % 14
print(word[num])
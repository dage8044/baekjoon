import sys
input = sys.stdin.readline
stack = []
N = int(input())
for i in range(N):
    word = list(map(int, input().rstrip('\n').split()))
    command = word[0]
    if command == 1:
        stack.append(word[1])
    elif command == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


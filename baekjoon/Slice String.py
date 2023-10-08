import sys
input = sys.stdin.readline

N = int(input().rstrip())
word_division = input().rstrip().split()
M = int(input().rstrip())
int_division = input().rstrip().split()
K = int(input().rstrip())
hap = input().rstrip()
S = int(input().rstrip())
word = input().rstrip()
result = []
temp = str()
word_division = [ i for i in word_division if i not in hap]
int_division = [ i for i in int_division if i not in hap]

for i in word:
    if i not in word_division and i not in int_division and i != ' ':
        temp += i
    else:
        if temp == '':
            pass
        else:
            result.append(temp)
            temp = str()

for i in result:
    print(i)
if temp != '':
    print(temp)
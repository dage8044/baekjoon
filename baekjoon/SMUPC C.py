import sys
input = sys.stdin.readline

morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9', '--..--': ',',
    '.-.-.-': '.', '..--..': '?', '---...': ':', '-....-': '-',
    '.--.-.': '@'
}

N = int(input().rstrip())
word = []
morse = input().rstrip().split()

for i in range(N):
    word.append(morse_code[morse[i]])
    
print(*word, sep='')
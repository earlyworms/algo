import sys 
sys.stdin = open('input.txt')

left = list(sys.stdin.readline().rstrip())
right = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'P':
        strlist = left.append(command[-1])
    elif command[0] == 'L' and len(left) != 0:
        right.append(left.pop())
    elif command[0] == 'D' and len(right) != 0:
        left.append(right.pop())
    elif command[0] == 'B' and len(left) != 0:
        left.pop()

answer = left + right[::-1]
print(''.join(answer))
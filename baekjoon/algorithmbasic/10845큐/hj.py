import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

from collections import deque

queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft()) if len(queue) != 0 else print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0) if len(queue) != 0 else print(1)
    elif command[0] == 'front':
        print(queue[0]) if len(queue) != 0 else print(-1)
    elif command[0] == 'back':
        print(queue[-1]) if len(queue) != 0 else print(-1)
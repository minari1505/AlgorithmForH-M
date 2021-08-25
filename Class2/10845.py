import sys
from collections import deque
N = int(sys.stdin.readline())
stack = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    if command[0] == "front":
       if len(stack) == 0:
           print(-1)
       else:
            print(stack[0]) 
    elif command[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if len(stack) ==0 :
            print(1)
        else:
            print(0)
    if command[0] =='pop':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[0])
            stack.popleft()
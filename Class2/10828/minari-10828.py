# 정수를 저장하는 스택 구현 (FILO)
import sys

stack = []
def push(X):
    stack.append(X)

def pop():
    if len(stack) != 0 :
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    if len(stack) != 0:
        return 0
    else:
        return 1

def top():
    if len(stack) != 0:
        return stack[-1]
    else:
        return -1

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push":
        push(command[1])
    if command[0] == "pop":
        print(pop())
    if command[0] == "size":
        print(size())
    if command[0] == "empty":
        print(empty())
    if command[0] == "top":
        print(top())

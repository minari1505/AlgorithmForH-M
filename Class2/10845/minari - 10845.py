# 큐 LIFO
import sys
queue = []
def push(X):
    queue.append(X)

def pop():
    if len(queue) != 0:
        return queue.pop(0)
    else:
        return -1

def size():
    return len(queue)

def empty():
    if len(queue) != 0:
        return 0
    else:
        return 1

def front():
    if len(queue) != 0:
        return queue[0]
    else:
        return -1

def back():
    if len(queue) != 0:
        return queue[-1]
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
    
    if command[0] == "front":
        print(front())
    
    if command[0] == "back":
        print(back())
    
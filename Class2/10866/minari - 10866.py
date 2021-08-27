# 덱(Deque)

import sys
deque = []
def push_front(X):
    deque.insert(0, X)

def push_back(X):
    deque.append(X)

def pop_front():
    return deque.pop(0) if len(deque) != 0 else -1

def pop_back():
    return deque.pop() if len(deque) != 0 else -1

def size():
    return len(deque)

def empty():
    return 0 if len(deque) != 0 else 1

def front():
    return deque[0] if len(deque) != 0 else -1

def back():
    return deque[-1] if len(deque) != 0 else -1

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push_front":
        push_front(command[1])
    
    if command[0] == "push_back":
        push_back(command[1])
        
    if command[0] == "pop_front":
        print(pop_front())
    
    if command[0] == "pop_back":
        print(pop_back())

    if command[0] == "size":
        print(size())
    
    if command[0] == "empty":
        print(empty())
    
    if command[0] == "front":
        print(front())
    
    if command[0] == "back":
        print(back())

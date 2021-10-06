# 집합
import sys
input = sys.stdin.readline
 
set_remove = set()
 
def add(x):
    set_remove.add(x)
 
def remove(x):
    set_remove.discard(x)
 
def check(x):
    if x in set_remove:
        return 1
    return 0
 
def toggle(x):
    if x in set_remove:
        set_remove.discard(x)
    else:
        set_remove.add(x)
 
def set_all():
    global set_remove
    set_remove = {i for i in range(1, 21)}
 
def empty():
    set_remove.clear()
 
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'add':
        add(int(command[1]))
    elif command[0] == 'remove':
        remove(int(command[1]))
    elif command[0] == 'check':
        print(check(int(command[1])))
    elif command[0] == 'toggle':
        toggle(int(command[1]))
    elif command[0] == 'all':
        set_all()
    else:
        empty()
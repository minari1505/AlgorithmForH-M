import sys
n = int(sys.stdin.readline())
list = [int(sys.stdin.readline().strip()) for i in range(n)]
list.sort()
for j in list:
    print(j)
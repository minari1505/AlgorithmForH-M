import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline().strip()) for i in range(n)]
li.sort()
for j in li:
    print(j)
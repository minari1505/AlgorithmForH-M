import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())
yosepus=deque([])
for i in range(1,N+1):
    yosepus.append(i)
print('<',end='')
while yosepus:
    for i in range(K-1):
        yosepus.append(yosepus[0])
        yosepus.popleft()
    print(yosepus.popleft(),end='')
    if yosepus:
        print(', ',end='')
print('>')

    
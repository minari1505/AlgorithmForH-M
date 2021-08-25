import sys
N, K = map(int,sys.stdin.readline().split())
yosepus = list(range(1,N+1))
print(yosepus)
while(len(yosepus)!=0):
    del yosepus[K]
    
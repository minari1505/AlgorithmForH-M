#1010 다리 놓기 Silver 5
from sys import stdin
n = int(stdin.readline())
cnt =0
def factori(n):
    if n ==1 or n ==0:
        return 1    #return n (X) n이 0일때 divide 0 error 출력
    else:
        return n *factori(n-1)
def nCm(n,m):
    return factori(n) // (factori(n-m) * factori(m))
for _ in range(n):
    a,b = map(int,stdin.readline().split())
    print(nCm(b,a))

#소수구하기
import sys
m,n = map(int,sys.stdin.readline().split())
def prime_number(x):
    if x ==2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
for j in range(m,n+1):
    if prime_number(j):
        print(j)
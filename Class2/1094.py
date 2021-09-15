#1094 막대기 Silver 4
from sys import stdin
n = int(stdin.readline())
cnt =0
while n!=0:
    if n %2 ==1:
        cnt +=1
    n = n //2
print(cnt)

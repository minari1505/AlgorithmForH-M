#1476 날짜 계산 Silver 5
from sys import stdin
e,s,m = map(int,stdin.readline().split())
year =1
while 1:
    if ((year-e)%15 == 0 and (year-s)%28 == 0 and (year-m)%19==0):
        break
    year +=1
print(year)

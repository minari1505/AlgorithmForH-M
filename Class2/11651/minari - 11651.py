#2차원 배열
#1. 2차원 배열로 입력받기
#2. lst[i][1]을 오름차순으로 정렬
#3. if lst[i][1] == lst[i+1][1] , lst[][1]을 오름차순으로 정렬
import sys
N = int(input())
#1.
lst = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    lst.append([x,y])
#2,3
lst.sort()

for i in range(len(lst)):
    print("{0} {1}".format(lst[i][0],lst[i][1]))

import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))
li.sort(key=lambda x:(x[1], x[0])) 
#li.sort(key=lambda x:x[1]) 
for j in li:
    print(j[0],j[1])
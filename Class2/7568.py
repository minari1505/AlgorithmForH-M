import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))
for j in range(n):
    count =1
    for k in range(n):
        if (li[j][0] < li [k][0] and li[j][1] < li[k][1]):
            count +=1
    print(count, end= " ")
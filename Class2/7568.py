import sys
n = int(sys.stdin.readline())
li = []
count =[]
for i in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))
for _ in range(n):
    count.append(1)
for j in range(n):
    for k in range(n):
        if (li[j][0] < li [k][0] and li[j][1] < li[k][1]):
            count[j] +=1
#print(count, end=" ")
for a in count:
    print(a)
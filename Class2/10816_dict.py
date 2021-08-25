from sys import stdin
a = int(input())
acard = list(map(int,stdin.readline().split()))
dic = dict()
for i in acard:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
b = int(input())
bcard = list(map(int,stdin.readline().split()))

for j in bcard:
    try:
        print(dic[j], end=" ")
    except:
        print(0, end=" ")

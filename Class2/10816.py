import sys
a = int(sys.stdin.readline())
acard = list(map(int,sys.stdin.readline().split()))
b = int(sys.stdin.readline())
bcard = list(map(int,sys.stdin.readline().split()))
count = [0] * b
j =0
for i in bcard:
    count[j] = acard.count(i)
    j+=1
for c in range(len(count)):
    print(count[c], end=" ")
n=int(input())
a = map(int,input().split())
b=sorted(list(set(a)))
for i in b:
    print(i,end=' ')

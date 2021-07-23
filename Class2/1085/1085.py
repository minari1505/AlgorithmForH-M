li = list(map(int,input().split()))
li[2]=li[2]-li[0]
li[3]=li[3]-li[1]
min=li[0]
for i in range(1,len(li)):
    if min > li[i]:
        min = li[i]
print(min)
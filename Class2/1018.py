n,m = map(int,input().split())
c=0
for i in range(m):
    i = input()
    for j in range(1,n):
        print(i[j])
        if i[j-1] == i[j]:
            if i[j] == 'B':
                i[j] = 'W'
        else:
            i[j]='B'
            c+=1
    
print(c)

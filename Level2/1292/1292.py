a,b = map(int,input().split())
c=[]
for i in range(1,b//2+2):
    c+=[i] *i

print(sum(c[a-1:b]))
'''
for j in range(a-1,b):
    sum += c[j]
print(sum)
'''

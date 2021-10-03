a=[]
for i in range(8):
    a.append(int(input()))
s = sorted(a,reverse=True)
sum = 0
b = []
for i in range(5):
    sum+=s[i]
    b.append(a.index(s[i])+1)
b_s = sorted(b)
print(sum)
for i in b_s:
    print(i,end=' ')

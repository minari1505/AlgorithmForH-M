#1475 방 번호 Silver 5

n = input()
a = [0] *10
for j in n:
    i = int(j)
    if i == 6:
        if a[6] > a[9]:
            a[9] +=1
            continue
    elif i==9:
        if a[9] > a[6]:
            a[6] +=1
            continue
    a[i] +=1 
print(max(a))

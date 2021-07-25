n,k = map(int,input().split())
up = n
down = k
for i in range(1,k):
    up = up * (n -i)
    down= down * (k-i)
print(up//down)
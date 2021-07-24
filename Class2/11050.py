n,k = map(int,input().split())
for i in range(1,k):
    k= k * (k-i)
    n = n * (n -i)
    print("n [%d]: ",i,n)
    print("k [%d]: ",i, k)

print(n)
print(k)
print(n//k)
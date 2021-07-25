a,b = map(int,input().split())
def gcd(a,b):
    if a <b :
        (a,b)=(b,a)
    while b!=0:
        (a,b)=(b,a%b)
    return a
gcd = int(gcd(a,b))
print(gcd)
print((a*b)// gcd)
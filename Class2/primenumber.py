def solutions(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                a[j] = False
    print(primes)

def solutions2(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j  in range(i+i, n,i):
                sieve[j]= False
    return [ i for i in range(2,n+1) if sieve[i]==True]

solutions(13)
print(solutions2(13))
# 이항 계수 1

```python
def factorial(n):
    a = 1
    for i in range(2,n+1):
        a *= i
    return a

N,K = map(int,input().split())
print(int((factorial(N))/(factorial(N-K)*factorial(K))))
```


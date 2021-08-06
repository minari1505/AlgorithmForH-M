# 최대공약수와 최소공배수

```python
#1. 두 개의 자연수 입력
#2. 최대공약수, 최소공배수 출력

# 최대공약수 : 유클리드호제법 이용해보기
# 최소공배수 : 두 값 곱한 후 최대공약수로 나누기

from math import gcd
A,B = map(int,input().split())
print(gcd(A,B))
print(int(A*B/gcd(A,B)))
```

```python
def gcd(A,B):
    while B!=0:
        A,B = B,A%B
    return A
A,B = map(int,input().split())
print(gcd(A,B))
print(int(A*B/gcd(A,B)))

#24 18 = 18, 6
#18 6 = 6 0
#6

```


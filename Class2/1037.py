#1037 약수 Silver 5
from sys import stdin
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a_sort = sorted(a)
if n>1:
    res = a_sort[0] * a_sort[-1]
else:
    res = a[0] * a[0]
print(res)

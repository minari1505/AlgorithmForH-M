from sys import stdin
n, k =map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
s = sorted(a)
print(s[k-1])
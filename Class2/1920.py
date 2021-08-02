from sys import stdin, stdout
n = int(input())
a = list(map(int,stdin.readline().split()))
m = int(input())
b = list(map(int,stdin.readline().split()))
for i in b:
    stdout.write('1\n') if i in a else stdout.write('0\n')
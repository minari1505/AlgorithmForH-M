#2563 색종이 Silver 5
n = int(input())
#3,7 -> 13,17
#5,2 -> 15,12
#15,7 -> 25,17
arr = [[0 for _ in range(101)] for _ in range(101)]
for i in range(n):
    a, b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j]=1
count = 0
for row in arr:
    count += row.count(1)
print(count)
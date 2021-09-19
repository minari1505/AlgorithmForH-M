#11728 배열합치기 Silver 5
a,b = map(int,input().split())
arr = sum([list(map(int,input().split())) for row in range(2)],[])
arr2 = sorted(arr)
for i in arr2:
    print(i,end=' ')

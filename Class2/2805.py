import sys
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
start = 1
end = max(a)

while start <= end:
    mid = (start+end) //2
    tmp = 0
    tmp = sum( x -mid if x -mid >= 0 else 0 for x in a)
    #for x in a:
     #   if x >= mid:
      #      tmp += x -mid
    if tmp >= m:
        start =mid +1
    else:
        end = mid -1
print(end)
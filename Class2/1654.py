import sys
K, N = map(int,sys.stdin.readline().split())
lan = list(int(sys.stdin.readline()) for i in range(K))

start, end = 1, max(lan)

while start <= end:
    mid = (start + end)//2
    tmp=0
    for x in lan:
        tmp += x // mid
    if tmp < N:
        end = mid-1
    elif tmp >= N:
        start = mid+1

print(end)

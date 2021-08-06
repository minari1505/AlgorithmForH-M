import sys
n = int(sys.stdin.readline())
counting = [0] * 10000

for i in range(n):
    num = int(sys.stdin.readline())
    counting[num] += 1

for i in range(10000):
    if counting[i] !=0:
        for j in range(counting[i]):
            print(i)
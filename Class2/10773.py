import sys
n = int(sys.stdin.readline())
count = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0 :
        count.pop()
    else:
        count.append(num)
    
print(sum(count))
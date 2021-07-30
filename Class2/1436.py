import sys
n = int(sys.stdin.readline())
six= 666
count = 0
while True:
    if '666' in str(six):
        count +=1
    if count == n:
        print(six)
        break
    six +=1
#print(n*1000-334)
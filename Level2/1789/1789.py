n = int(input())
sum=0
cnt =0
i =1
while 1:
    sum += cnt
    if sum > n:
        print(cnt-1)
        break
    elif sum ==n:
        print(cnt)
        break
    cnt+=1
    print(cnt)
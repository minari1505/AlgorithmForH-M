#뒤집기
s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt +=1
print((cnt+1)//2)
####숏코딩
v = input().count
print((v('10')+v('01')+1)//2)

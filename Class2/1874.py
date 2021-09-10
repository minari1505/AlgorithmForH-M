import sys
N = int(sys.stdin.readline())
a = []
b =[]
count =1
flag= True
for i in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        #a 리스트에 입력한 숫자까지의 숫자들 모두 입력해야됨
        a.append(count)
        b.append('+')
        count +=1
    if a[-1] == num:
        a.pop()
        b.append('-')
    else:
        flag =False
if flag == False:
    print("NO")
else:
    for i in b:
        print(i)
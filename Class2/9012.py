n = int(input())
for i in range(n):
    line = input()
    answer = 0
    for a in line:
        if a == "(":
            answer +=1
        elif a == ")":
            answer -=1
        if answer <0:
            print("NO")
            break
    if answer > 0:
        print("NO") 
    elif answer ==0:
        print("YES")
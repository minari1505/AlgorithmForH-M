n=int(input())
for i in range(1,n+1):
    div_num=list(map(int,str(i)))
    print("div_num",div_num)
    sum_num =i + sum(div_num)
    print("sum_num: ",sum_num)
    if(sum_num==n):
        print_num = i
        break
print(print_num)
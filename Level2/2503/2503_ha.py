import sys
from itertools import permutations
n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9],3))
print(len(num))
print(num)
for _ in range(n):
    test,s,b = map(int,input().split())
    test = list(str(test))    #test int to str per position, then tolist
    cnt = 0
    for i in range(len(num)):
        s_cnt = b_cnt =0
        i -= cnt

        for j in range(3):          #Because of test(three)
            test[j] = int(test[j])
            if test[j] in num[i]:   
                if j == num[i].index(test[j]):      #If position of num[i] for test[j] is j index same, strike count
                    s_cnt +=1
                else:
                    b_cnt +=1
        if s_cnt != s or b_cnt !=b:
            num.remove(num[i])
            cnt +=1
print(len(num))

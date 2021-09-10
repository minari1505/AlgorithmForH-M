import math
n = int(input())
"""
dp = [0,1]
for i in range(2,n+1):
    min_value = 1e9
    j =1
    while (j**2) <= i :
        min_value = min(min_value,dp[i-(j**2)])
        j +=1

    dp.append(min_value +1)
print(dp[n])
"""
def four_squares(n):
    if (n ** 0.5).is_integer():
        return 1
    for i in range(1,int(n**0.5) +1):
        if n < i ** 2:
            break
        if ((n- i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1,int(n**0.5)+1):
        if n < i **2:
            break
        for j in range(1,int((n -i **2) **0.5)+1):
            if n < i **2 + j **2:
                break
            if (( n- i **2 - j**2) **0.5).is_integer():
                return 3
    return 4
print(four_squares(n))

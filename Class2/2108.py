import sys
from collections import Counter
def count_num(data):
    cnt_list = Counter(data).most_common()
    print(cnt_list)
    if len(cnt_list) >1 and cnt_list[0][1] == cnt_list[1][1]:
        return cnt_list[1][0]
    else:
        return cnt_list[0][0]

def mean(data):
    return round(sum(data)/ len(data))
def mid(data):
    data.sort()
    middium = data[len(data)//2]
    return middium
def cha(data):
    return max(data)- min(data)

n =int(sys.stdin.readline())
#stat = [int(sys.stdin.readlines().strip() for i in range(n))]
stat = []
for i in range(n):
    stat.append(int(sys.stdin.readline()))


print(mean(stat))
print(mid(stat))
print(count_num(stat))
print(cha(stat))
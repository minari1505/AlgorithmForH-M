import sys
n=int(input())
line = [sys.stdin.readline().strip() for i in range(n)]
set_line=set(line)
line = list(set_line)
line.sort()
line.sort(key=len)
for i in line:
    print(i)
#dic = {}
#print(dic.items())
#print(sorted(dic.items(),key=lambda x : x[1]))
#for key in dic.keys():
#    print(key)

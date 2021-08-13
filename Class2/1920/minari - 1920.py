import sys
N = int(sys.stdin.readline())
N_lst = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_lst = list(map(int,sys.stdin.readline().split()))

count = [0 for i in range(M)]
for i in range(len(M_lst)):
    for j in N_lst:
        if M_lst[i] == j:
            count[i] = 1

for i in count:
    print(i)

        

import sys
num = int(sys.stdin.readline())
for _ in range(num):
    N, M= list(map(int,sys.stdin.readline().split()))
    K = list(map(int,sys.stdin.readline().split()))
    idx = list(range(N))
    idx[M]='target'
    order = 0
    while True:
        if K[0] == max(K):
            order +=1
            if idx[0]=='target':
                print(order)
                break
            else:
                K.pop(0)
                idx.pop(0)
        else:
            K.append(K.pop(0))
            idx.append(idx.pop(0))

#K 번째 수
N,K = map(int,input().split())
S = list(map(int,input().split()))
S.sort()
print(S[K-1])
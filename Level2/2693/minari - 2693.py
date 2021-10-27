# N번째 큰 수

#배열 A가 주어질 때 N번째 큰 값을 출력하기, 배열A는 10개, N = 3
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    A = list(map(int,sys.stdin.readline().split()))
    A.sort(reverse=True)
    print(A[2])
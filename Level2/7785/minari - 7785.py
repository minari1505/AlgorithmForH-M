# 회사에 있는 사람
# 로그가 주어졌을 때, 지금 회사에 있는 모든 사람 구하기

# leave가 없는 이름만 출력하기 , 사전의 역순으로 -> 내림차순

import sys
n = int(sys.stdin.readline())
name_lst = set() # name_lst를 중복 불가한 set 함수로 설정

#이름과 출퇴근기록 받기, 만약 퇴근했다면 name_lst에서 이름삭제
for _ in range(n):
    name,record = map(str,input().split())
    name_lst.add(name)
    if record == "leave":
        name_lst.remove(name)

#name_lst가 집합이므로 순서가 없다. 사전의 역순으로 출력해야하기 때문에 list로 구조 변경
name_lst = list(name_lst)
name_lst.sort(reverse=True) # 내림차순 정렬

for i in name_lst:
    print(i)

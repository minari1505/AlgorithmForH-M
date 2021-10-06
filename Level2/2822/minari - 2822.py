# 점수계산

# 총 8개문제풀이. 경과한 시간순으로 점수 얻음. 못풀면 0점
# 총점 : 높은 점수 5개의 합

# 입력 : 각 문제 점수 주어짐 (8줄)
# 출력 : 총점,어떤 문제가 최종 점수에 포함되었는지

#1. 문제 점수가 주어지는대로 리스트에 추가
#2. 리스트 sorted(내림차순) (리스트 복사 후 정렬)


score = []
order = []
#1.
for _ in range(8):
    score.append(int(input()))

score_c = sorted(score,reverse=True) #2.

print(sum(score_c[:5])) #리스트 max값 출력

#score_c 중 큰 값 5개의 값을 가진 index +1 (문제번호가 1~8이기 때문에 +1) 을 order에 저장
for i in range(5):
    order.append(score.index(score_c[i])+1)

order.sort()

for j in order:
    print(j,end = " ")
#블랙잭 순열 조합 라이브러리 사용 복습 필요
from itertools import combinations 
card_num, target_num = map(int,input().split())
card_list = list(map(int,input().split()))
biggest_num = 0

for cards in combinations(card_list,3):
    temp_sum = sum(cards)
    if biggest_num < temp_sum <= target_num:
        biggest_num = temp_sum
        print(biggest_num)
print(biggest_num)
#person 리스트로 풀면 시간초과 set으로 딕셔너리형으로 
person={}
for _ in range(int(input())):
    p, c = input().split()
    if c=='enter':
        person[p]= 'enter'
    else:
        del person[p]
    print(person)
for i in sorted(person.keys(),reverse=True):
    print(i)

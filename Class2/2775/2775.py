n = int(input())
for _ in range(n): 
    layer = int(input())
    room = int(input())
    people=[i for i in range(1,room+1)] 
    for la in range(layer):
        for ro in range(1,room):
            people[ro] += people[ro-1]
            print(people)
    print(people[-1])
from sys import stdin
n = int(stdin.readline())
s =[]
for i in range(n):
    command = stdin.readline().split()
    if len(command) == 1:
        if command[0] == 'all':
            s = list(range(1,21))
        elif command[0] =='empty':
            s = []
    else:
        num = int(command[1])
        if command[0] == 'add' and not num in s:
            s.append(num)
        elif command[0] == 'remove'and num in s:
            s.remove(num)
        elif command[0] == 'check':
            if num in s:
                print("1")
            else:
                print("0")
        elif command[0] == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.append(num)
    print(s)
    
        

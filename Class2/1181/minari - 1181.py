# 단어정렬

```python
#길이가 짧은 것부터(sort(key=lambda a:len(a))) 길이가 같다면 사전순(sort())
N = int(input())#단어 개수
lst = []
for i in range(N):
    lst.append(input())
lst.sort()
lst.sort(key=lambda a:len(a))
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
for j in range(len(new_lst)):
    print(new_lst[j])
```


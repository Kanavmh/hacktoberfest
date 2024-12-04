n = list(map(int, input().split()))
a = []
for i in range(n[1]):
     arr = list(map(float, input().split()))
     a.append(arr)
zipped = zip(*a)
for group in zipped:
    print(sum(group)/len(group))

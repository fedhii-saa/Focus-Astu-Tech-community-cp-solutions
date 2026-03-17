i = int(input())
count = 0
for j in range(i):
    a, b, c = map(int,input().split())
    if a+b+c >= 2:
        count += 1
print(count)

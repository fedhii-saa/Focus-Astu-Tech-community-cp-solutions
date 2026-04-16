t = int(input())
names = []
freq = {}
for i in range(t):
    name = input()
    names.append(name)
    
for n in names:
    if n not in freq:
        print("OK")
        freq[n] = 1
    else:
        print(n + str(freq[n]))
        freq[n] += 1

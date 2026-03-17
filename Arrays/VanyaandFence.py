n,h = map(int, input().split())
nums = list(map(int, input().split()))
w = sum(1 if x<=h else 2 for x in nums)
print(w)

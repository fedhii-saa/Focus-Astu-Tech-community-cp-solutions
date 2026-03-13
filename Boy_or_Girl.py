name = input().strip()
char = set(name)
print("CHAT WITH HER!" if len(char)%2==0 else "IGNORE HIM!")

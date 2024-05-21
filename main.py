a = list(map(int, input().split()))
b = sum(c ** 2 for c in a if c % 2 != 0)
print(b)

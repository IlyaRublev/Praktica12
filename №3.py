with open('lines.txt', 'r') as file:
    a = file.readlines()
a = [b.strip() for b in a]
c = sorted(a, key=lambda x: (-len(x), x))
for b in c:
    print(b)
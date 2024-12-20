with open('input.txt', 'r') as f:
    lines = f.readlines()
    reports = [list(map(int, line.strip().split())) for line in lines]

def is_safe(level):
    return ((all(x < y for x, y in zip(level, level[1:])) or 
         all(x > y for x, y in zip(level, level[1:]))) and 
        all(1 <= abs(x - y) <= 3 for x, y in zip(level, level[1:])))

count = 0
for level in reports:
    if is_safe(level):
        count += 1

print(count)
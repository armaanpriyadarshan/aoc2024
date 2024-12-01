with open('input.txt', 'r') as file:
    l1, l2 = zip(*(sorted(map(int, line.split())) for line in file))

distance = sum(abs(a - b) for a, b in zip(l1, l2))
print(distance)
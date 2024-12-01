from collections import Counter

with open('input.txt', 'r') as file:
    l1, l2 = zip(*(map(int, line.split()) for line in file))
    
similarity = sum(a * Counter(l2)[a] for a in l1)
print(similarity)
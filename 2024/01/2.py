left = []
right = []

with open("input.txt", "r") as f:
    for line in f:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))

# similarity score
total = 0
for i in range(len(left)):
    for j in range(len(right)):
        count = 0
        if left[i] == right[j]:
            count += 1

        score = left[i] * count
        total += score


print(total)

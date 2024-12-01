# line strip and split to create left and right list
left = []
right = []
with open("input.txt", "r") as f:
    for line in f:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))

# sort them
left.sort()
right.sort()

# create a loop to calculate difference and sum diff.
total = 0
for i in range(len(left)):
    diff = abs(left[i] - right[i])
    total += diff

print(total)

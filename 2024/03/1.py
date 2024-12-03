import re


with open("input.txt", "r") as f:
    text = f.read()


# detct mul(num1, num2) with regex.
# number should be 1-3 digit numbers.
pattern = r"mul\(\d{1,3}\,\d{1,3}\)"
mulMatch = re.findall(pattern, text)


result = 0
for i in mulMatch:
    # for 1 digit numbers.
    # mul = int(i[4]) * int(i[-2])
    xy = i[4:-1].split(",")
    x = int(xy[0].strip())
    y = int(xy[1].strip())
    result += x * y

print(result)

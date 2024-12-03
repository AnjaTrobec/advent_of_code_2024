# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

FILE = "Day 2/data.csv"

def read_file():
    with open(FILE) as file:
        return [list(map(int, line.split())) for line in file.read().splitlines()] #splitlines() == split("\n")

print(read_file())

def check_conditions():
    safe = 0
    file = read_file()
    for line in file:
        if all(line[i] <= line[i + 1] for i in range(len(line) - 1)) or all(line[i] >= line[i + 1] for i in range(len(line) - 1)): #all() check the condition on every element in the list
            if all(1 <= abs(line[i + 1] - line[i]) <= 3 for i in range(len(line) - 1)):
                safe += 1
    return safe

print(check_conditions())


def check_conditions2():
    safe = 0
    file = read_file()
    d = {n: False for n,_ in enumerate(file)}
    for n, line in enumerate(file):
        for i, x in enumerate(line):
            l = line[:i] + line[i+1:]
            if all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1)): #all() check the condition on every element in the list
                if all(1 <= abs(l[i + 1] - l[i]) <= 3 for i in range(len(l) - 1)):
                    d[n] = True
    return sum(d.values())

print(check_conditions2())

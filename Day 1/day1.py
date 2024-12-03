# day 1

FILE = "Day 1/data.csv"

def read_file():
    with open(FILE) as file:
        lines = file.read().splitlines()
        return [(int(x), int(y)) for line in lines for x, y in [line.split()]]

def result1(file):
    l1 = sorted([line[0] for line in file])
    l2 = sorted([line[1] for line in file])
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))

print("Result:", result1(read_file()))

def similarity_dict(file):
    l1 = [line[0] for line in file]
    l2 = [line[1] for line in file]
    counts = {x: l2.count(x) for x in set(l2)}
    return {x: counts[x] for x in l1 if x in counts}

def result2(file):
    l1 = [line[0] for line in file]
    similarity = similarity_dict(file)
    return sum(x * similarity.get(x, 0) for x in l1)

print(result2(read_file()))

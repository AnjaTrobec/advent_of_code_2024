# Day 1

FILE = "Day 1/data.csv"

def read_file():
    with open(FILE) as file:
        return [tuple(map(int, line.split())) for line in file.read().splitlines()]

# PART 1
def result1(file):
    l1, l2 = zip(*file)
    l1, l2 = sorted(l1), sorted(l2)
    return sum(abs(a - b) for a, b in zip(l1, l2))

file_data = read_file()
print("Result1:", result1(file_data))

# PART 2
def similarity_dict(file):
    l2_counts = {}
    for _, y in file:
        l2_counts[y] = l2_counts.get(y, 0) + 1
    return {x: l2_counts.get(x, 0) for x, _ in file}

def result2(file):
    similarity = similarity_dict(file)
    return sum(x * similarity[x] for x, _ in file)

print("Result2:", result2(file_data))

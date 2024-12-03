import re

FILE = "Day 3/data.csv"

def extract_mul(content: str) -> list[tuple[int, int]]:
    return re.findall(r'mul\((\d+),(\d+)\)', content)

def calculate_sum_of_products(matches: list[tuple[str, str]]) -> int:
    return sum(int(x) * int(y) for x, y in matches)

def part1(content: str) -> int:
    matches = extract_mul(content)
    return calculate_sum_of_products(matches)

def part2(content: str) -> int:
    start_marker = re.escape("do()")
    end_marker = re.escape("don't()")

    sections = re.findall(fr'{start_marker}(.*?){end_marker}', content, re.DOTALL)
    
    all_matches = [match for section in sections for match in extract_mul(section)]
    return calculate_sum_of_products(all_matches)

def main():
    with open(FILE, 'r') as file:
        content = file.read()
    
    total_sum = part1(content)
    print(f"Part 1: {total_sum}")

    conditional_sum = part2(content)
    print(f"Part 2: {total_sum - conditional_sum}")
    

if __name__ == "__main__":
    main()

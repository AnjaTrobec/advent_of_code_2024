import re

FILE = "Day 3/data.csv"

def part1():
    with open(FILE, 'r') as file:
        content = file.read()  
        matches = re.findall(r'mul\((\d+),(\d+)\)', content)  
        return sum(int(x) * int(y) for x, y in matches)

print(part1())

def part2():
    with open(FILE, 'r') as file:
        content = file.read() 
        enable = "do()"
        disable = "don't()"
        s = re.escape(enable)
        e = re.escape(disable) 

        sections = re.findall(fr'{e}(.*?){s}', content, re.DOTALL)
        
        all_matches = []
        for section in sections:
            matches = re.findall(r'mul\((\d+),(\d+)\)', section)
            all_matches.extend(matches)
        
        return sum([int(x) * int(y) for x, y in all_matches])
    
print(part1() - part2())
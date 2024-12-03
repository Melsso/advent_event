import re

def mul_sum(data):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)
    ans = 0
    for match in matches:
        x = int(match[0])
        y = int(match[1])
        ans += x * y
    return ans

def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()

data = load_file('file.txt')
result = mul_sum(data)
print(f"Result of the sum of multiplications: {result}")

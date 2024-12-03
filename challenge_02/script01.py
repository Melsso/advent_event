import re

def mul_sum(data):
    pattern = r'mul\((\d+),(\d+)\)'
    ans = 0
    mul_on = True
    instructions = re.split(r'(\w+\(\d+,\d+\))', data)
    for instruction in instructions:
        if "do()" in instruction:
            mul_on = True
        elif "don't()" in instruction:
            mul_on = False
        elif "mul(" in instruction and mul_on:
            match = re.search(pattern, instruction)
            if match:
                x = int(match[1])
                y = int(match[2])
                ans += x * y

    return ans

def load_data(file_path):
    with open(file_path, 'r') as file:
        return file.read()  

file_path = 'file.txt'  
data = load_data(file_path)
result = mul_sum(data)
print(f"Result of the sum of multiplications: {result}")

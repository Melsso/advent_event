def distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total = 0
    for left, right in zip(left_list, right_list):
        total += abs(left - right)
    
    return total

left_list = []
right_list = []
with open("file.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

result = distance(left_list, right_list)
print("Total Distance:", result)

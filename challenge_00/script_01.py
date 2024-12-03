from collections import Counter

left_list = []
right_list = []

with open("file.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

right_count = Counter(right_list)

similarity_score = 0
for num in left_list:
    similarity_score += num * right_count.get(num, 0)

print("Similarity Score:", similarity_score)

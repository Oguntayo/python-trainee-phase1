import random
from collections import Counter

rows = [
    'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE',
    'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE',
    'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'
]

clean_map = {"BLEW": "BLUE", "ARSH": "ASH"}
colors = [
    clean_map.get(c.strip().upper(), c.strip().upper())
    for row in rows
    for c in row.split(",")
]

print("Total colors:", len(colors))


color_count = Counter(colors)
print("\nColor Frequency")
print(color_count)

most_common_color = color_count.most_common(1)[0]
print("\nMost worn color:", most_common_color)

sorted_colors = sorted(colors)
median_color = sorted_colors[len(sorted_colors)//2]
print("\nMedian color:", median_color)


unique_colors = sorted(set(colors))
color_to_num = {color: i+1 for i, color in enumerate(unique_colors)}
numbers = [color_to_num[c] for c in colors]
mean = sum(numbers)/len(numbers)
variance = sum((x - mean)**2 for x in numbers)/len(numbers)
print("\nVariance:", variance)


prob_red = colors.count("RED") / len(colors)
print("\nProbability of RED:", prob_red)


def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index+1)

numbers_list = [2,5,7,10,14,20]
print("\nRecursive Search 10:", recursive_search(numbers_list,10))


random.seed(0) 
binary = ''.join(random.choice("01") for _ in range(4))
decimal = int(binary,2)
print("\nRandom Binary:", binary)
print("Decimal:", decimal)

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b

total = sum(fibonacci(50))
print("\nSum first 50 Fibonacci:", total)
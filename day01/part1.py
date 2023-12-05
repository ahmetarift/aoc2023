digit_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def detect_digits(text: str):
    return [digit_dict[char] for char in text if char in digit_dict.keys()] 

with open("aoc2023/day01/example.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        digit_list = detect_digits(text)
        total = total + 10 * digit_list[0] + digit_list[-1]
    assert total == 142

with open("aoc2023/day01/input.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        digit_list = detect_digits(text)
        total = total + 10 * digit_list[0] + digit_list[-1]
    
print(total)

    
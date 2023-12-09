digit_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

string_digit_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                     "six": 6, "seven": 7, "eight": 8, "nine": 9}

def detect_digits(text: str):
    digits = []
    N = len(text)
    i = 0
    while (i < N):
        if text[i] in digit_dict.keys():
            digits.append(digit_dict[text[i]])
        elif text[i:i+3] in string_digit_dict.keys():
            digits.append(string_digit_dict[text[i:i+3]])
        elif text[i:i+4] in string_digit_dict.keys():
            digits.append(string_digit_dict[text[i:i+4]])
        elif text[i:i+5] in string_digit_dict.keys():
            digits.append(string_digit_dict[text[i:i+5]])
        i+=1
    return digits

with open("day01/example2.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        digit_list = detect_digits(text)
        total = total + 10 * digit_list[0] + digit_list[-1]
    assert total == 281

with open("day01/input.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        digit_list = detect_digits(text)
        total = total + 10 * digit_list[0] + digit_list[-1]
    
print(total)

    
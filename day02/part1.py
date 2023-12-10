capacity_dict = {"red": 12, "green": 13, "blue": 14}

def check_capacity(index: int, text: str) -> bool:
    tours = text.split(";")
    for tour in tours:
        colors = tour.split(",")
        for color in colors:
            color = color.strip()

            if " red" in color:
                red_number = color.split(' red')[0]
                if int(red_number) > capacity_dict["red"]:
                    return 0

            elif " green" in color:
                green_number = color.split(' green')[0]
                if int(green_number) > capacity_dict["green"]:
                    return 0
            
            elif " blue" in color:
                blue_number = color.split(' blue')[0]
                if int(blue_number) > capacity_dict["blue"]:
                    return 0
    
    return index

with open("day02/example.txt") as f:
    input_lines = [line.strip().split(":")[-1].strip() for line in f.readlines()]
    total = 0
    for i, text in enumerate(input_lines, 1):
        total += check_capacity(i, text)
    assert(total == 8)

with open("day02/input.txt") as f:
    input_lines = [line.strip().split(":")[-1].strip() for line in f.readlines()]
    total = 0
    for i, text in enumerate(input_lines, 1):
        total += check_capacity(i, text)
    print(total)
    

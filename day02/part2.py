def minimum_capacity(text: str) -> bool:
    tours = text.split(";")
    max_red = 0
    max_green = 0
    max_blue = 0

    for tour in tours:
        colors = tour.split(",")
        for color in colors:
            color = color.strip()

            if " red" in color:
                red_number = color.split(' red')[0]
                if int(red_number) > max_red:
                    max_red = int(red_number)

            elif " green" in color:
                green_number = color.split(' green')[0]
                if int(green_number) > max_green:
                    max_green = int(green_number)
            
            elif " blue" in color:
                blue_number = color.split(' blue')[0]
                if int(blue_number) > max_blue:
                    max_blue = int(blue_number)
    
    return max_red * max_green * max_blue

with open("day02/example.txt") as f:
    input_lines = [line.strip().split(":")[-1].strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        total += minimum_capacity(text)
    assert(total == 2286)

with open("day02/input.txt") as f:
    input_lines = [line.strip().split(":")[-1].strip() for line in f.readlines()]
    total = 0
    for text in input_lines:
        total += minimum_capacity(text)
    print(total)
    


# get_number = int(input("input a number to convert to binary: "))
# number_to_binary = bin(get_number)
# print(number_to_binary) #print output

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")

    if len(hex_color) != 6:
        raise ValueError("Expected a 6-digit hex color, e.g. #FF5733")

    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


color = hex_to_rgb(input("input hex numer: "))
print(color)  # (255, 87, 51)

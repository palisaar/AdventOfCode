def part_one():
    file1 = open('day_two.txt', 'r')
    lines = file1.readlines()

    depth = 0
    hori_pos = 0
    for instruction in lines:
        if instruction[0] == "d":
            depth += int(instruction[5])
            print(int(instruction[5]))
        elif instruction[0] == "u":
            depth -= int(instruction[3])
            print(int(instruction[3]))
        elif instruction[0] == "f":
            hori_pos += int(instruction[8])
            print(int(instruction[8]))
    print("hori_pos: ", hori_pos, " depth: ", depth, "multiplied: ", hori_pos * depth)

def part_two():
    file1 = open('day_two.txt', 'r')
    lines = file1.readlines()

    depth = 0
    hori_pos = 0
    aim = 0
    for instruction in lines:
        if instruction[0] == "d":
            aim += int(instruction[5])
        elif instruction[0] == "u":
            aim -= int(instruction[3])
        elif instruction[0] == "f":
            hori_pos += int(instruction[8])
            depth += aim * int(instruction[8])

    print("hori_pos: ", hori_pos, " depth: ", depth, "multiplied: ", hori_pos * depth)
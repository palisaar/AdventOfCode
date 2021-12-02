def day_one():
    print("part one: ", part_one())
    print("part two: ", part_two())


def part_one():
    file1 = open('day_one.txt', 'r')
    lines = file1.readlines()

    temp = 0
    count = 0
    for measurement in lines:
        if int(temp) < int(measurement) and int(temp) != 0:
            count += 1
        temp = measurement
    return count


def part_two():
    file1 = open('day_one.txt', 'r')
    lines = file1.readlines()

    window_current = 0
    temp2 = 0
    temp3 = 0
    count = 0
    for measurement in lines:
        window_old = window_current
        temp1 = temp2
        temp2 = temp3
        temp3 = measurement
        window_current = int(temp1) + int(temp2) + int(temp3)
        #print(int(temp1), " + ", int(temp2), " + ", int(temp3), " = ", window_current, " ", window_old)
        if int(window_old) < int(window_current) and int(temp1) != 0 and window_old != int(temp1) + int(temp2):
            count += 1
    return count
def part_one():
    file1 = open('day_three.txt', 'r')
    lines = file1.readlines()

    file_length = 0
    one_occ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for diagno in lines:
        file_length += 1
        for i in range(0, len(one_occ)):
            if int(diagno[i]) == 1:
                one_occ[i] += 1
    print(one_occ)
    print(file_length)

    for i in range(0, len(one_occ)):
        if one_occ[i] > file_length / 2:
            one_occ[i] = 1
        else:
            one_occ[i] = 0

    binary_string = l2s(one_occ)
    inverted_bs = "".join('1' if x == '0' else '0' for x in binary_string)

    print("Solution: ", int(binary_string, 2), " * ", int(inverted_bs, 2), " = ",
          int(binary_string, 2) * int(inverted_bs, 2))


def l2s(list1):
    string = ""

    for ele in list1:
        string += str(ele)

    return string

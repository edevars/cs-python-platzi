random_numbers = [28, 34, 52, 53, 60, 62, 73, 82, 85, 87, 97, 101, 116, 122, 138, 141, 154, 156, 167, 179, 187, 190, 191, 199, 212, 217, 219, 225, 227, 228, 233, 256, 269, 315, 319, 323, 324, 333, 336, 344, 346, 363, 381, 385, 389, 390, 417, 419, 422,
                  437, 438, 439, 450, 456, 516, 537, 563, 571, 595, 607, 614, 636, 648, 649, 653, 675, 679, 683, 684, 690, 700, 704, 722, 724, 726, 732, 734, 746, 754, 771, 789, 790, 791, 792, 795, 805, 808, 815, 844, 845, 853, 860, 874, 896, 901, 924, 949, 954, 993, 999]


target = int(input('Please select a number between 1 and 1000: '))

new_list = [*random_numbers]
steps = 0

while True:
    half = int(len(new_list)/2)
    steps += 1
    if target == new_list[half]:
        print(f"The value {new_list[half]} is in the list")
        print("Necesary steps: ", steps)
        break
    elif len(new_list) == 1 and new_list[0] != target:
        print("The value isn't in the list")
        print("Necesary steps: ", steps)
        break

    if target > new_list[half]:
        new_list = new_list[half:]
    else:
        new_list = new_list[0:half]

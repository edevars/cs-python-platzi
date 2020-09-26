# Binary search algorithm
def recursive_binary_search(numbers_list, target, left, right):
    if left <= right:
        mid = (right + left)//2

        if numbers_list[mid] == target:
            return mid
        elif numbers_list[mid] > target:
            return recursive_binary_search(numbers_list, target, left, mid - 1)
        else:
            return recursive_binary_search(numbers_list, target, mid + 1, right)
    else:
        return False


if __name__ == "__main__":
    random_numbers = [28, 34, 52, 53, 60, 62, 73, 82, 85, 87, 97, 101, 116, 122, 138, 141, 154, 156, 167, 179, 187, 190, 191, 199, 212, 217, 219, 225, 227, 228, 233, 256, 269, 315, 319, 323, 324, 333, 336, 344, 346, 363, 381, 385, 389, 390, 417, 419, 422,
                      437, 438, 439, 450, 456, 516, 537, 563, 571, 595, 607, 614, 636, 648, 649, 653, 675, 679, 683, 684, 690, 700, 704, 722, 724, 726, 732, 734, 746, 754, 771, 789, 790, 791, 792, 795, 805, 808, 815, 844, 845, 853, 860, 874, 896, 901, 924, 949, 954, 993, 999]

    target = int(input('Please select a number between 1 and 1000: '))
    index = recursive_binary_search(
        random_numbers, target, 0, len(random_numbers) - 1)
    if index:
        print(f"The number {target} is in the list with the index {index}")
    else:
        print("Number doesn't exist in the list")

# RACKSACK COMMON ITEM TYPE

def task_a(int_num_arr):
    counter = 0
    shared_items = []

    for line in int_num_arr:
        length = len(line)
        middle_index = length // 2
        compartment1 = line[:middle_index]
        compartment2 = line[middle_index:]
        for char in compartment1:
            if char in compartment2:
                shared_items.append(char)
                break
    for char in shared_items:
        if char.isupper():
            number = ord(char) - 38
            counter += number
        else:
            number = ord(char) - 96
            counter += number

    print("COUNTER: ", counter)
    return counter


def task_b(int_num_arr):
    counter = 0
    shared_items = []
    tmp_counter = 2
    sublistsize = 3

    for i in range(len(int_num_arr) - sublistsize + 1):
        if tmp_counter <= 1:
            tmp_counter += 1
            continue

        tmp_counter = 0
        sub_list = int_num_arr[i:i + sublistsize]
        rucksack1 = sub_list[0]
        rucksack2 = sub_list[1]
        rucksack3 = sub_list[2]

        for char in rucksack1:
            if char in rucksack2:
                if char in rucksack3:
                    shared_items.append(char)
                    break

    for char in shared_items:
        if char.isupper():
            number = ord(char) - 38
            counter += number
        else:
            number = ord(char) - 96
            counter += number

    print("COUNTER: ", counter)
    return counter

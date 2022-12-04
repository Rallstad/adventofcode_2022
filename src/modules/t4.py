# NUMBER OF OVERLAP

def task_a(int_num_arr):
    counter = 0
    for line in int_num_arr:
        first_elf = line.split(',')[0]
        second_elf = line.split(',')[1]
        first_number_first_elf = int(first_elf.split('-')[0])
        second_number_first_elf = int(first_elf.split('-')[1])
        first_number_second_elf = int(second_elf.split('-')[0])
        second_number_second_elf = int(second_elf.split('-')[1])

        if first_number_first_elf <= first_number_second_elf:
            if second_number_first_elf >= second_number_second_elf:
                counter += 1
                continue

        if first_number_second_elf <= first_number_first_elf:
            if second_number_second_elf >= second_number_first_elf:
                counter += 1
                continue

    print("NUMBER OF COMPLETE OVERLAP: ", counter)
    return counter


def task_b(int_num_arr):
    counter = 0
    for line in int_num_arr:
        first_elf = line.split(',')[0]
        second_elf = line.split(',')[1]
        first_number_first_elf = int(first_elf.split('-')[0])
        second_number_first_elf = int(first_elf.split('-')[1])
        first_number_second_elf = int(second_elf.split('-')[0])
        second_number_second_elf = int(second_elf.split('-')[1])

        if first_number_first_elf <= first_number_second_elf:
            if second_number_first_elf >= first_number_second_elf:
                counter += 1
                continue

        if first_number_second_elf <= first_number_first_elf:
            if second_number_second_elf >= first_number_first_elf:
                counter += 1
                continue

    print("NUMBER OF PARTIALLY OVERLAP: ", counter)
    return counter


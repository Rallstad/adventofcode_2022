# ELVES WITH MOST CALORIES

def task_a(int_num_arr):
    tmp = 0
    tmp_most_calories = 0
    for line in int_num_arr:
        if line == '':
            if tmp_most_calories <= tmp:
                tmp_most_calories = tmp
            tmp = 0
        else:
            tmp += int(line)
    print("MOST CALORIES: ", tmp_most_calories)
    return tmp_most_calories


def task_b(int_num_arr):
    calories_list = []
    tmp = 0
    tmp_most_calories = 0
    for line in int_num_arr:
        if line == '':
            calories_list.append(tmp)
            tmp = 0
        else:
            tmp += int(line)
    calories_list.sort()
    top_three_accumulated = calories_list[len(calories_list)-1] + calories_list[len(calories_list)-2] + calories_list[len(calories_list)-3]
    print("TOP THREE ACCUMULATED: ", top_three_accumulated)
    return top_three_accumulated

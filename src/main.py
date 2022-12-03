import utils.file_reader
from src.modules import t1, t2, t3, t4, t5, t6

tasknr = input('Type task number you want to run: ')
print(f'Running task {tasknr}')
inputf = f'./inputs/inputTask{tasknr}.txt'

try:
    int_num_arr = [line for line in utils.file_reader.read_file(inputf)]
    if int(tasknr) == 1:
        t1.task_a(int_num_arr)
        t1.task_b(int_num_arr)
    elif int(tasknr) == 2:
        t2.task_a(int_num_arr)
        t2.task_b(int_num_arr)
    elif int(tasknr) == 3:
        t3.task_a(int_num_arr)
        t3.task_b(int_num_arr)
    elif int(tasknr) == 4:
        t4.task_a(int_num_arr)
        t4.task_b(int_num_arr)
    elif int(tasknr) == 5:
        t5.task_a(int_num_arr)
        t5.task_b(int_num_arr)
    elif int(tasknr) == 6:
        t6.task_a(int_num_arr)
        t6.task_b(int_num_arr)
except:
    print("invalid input of: " + tasknr)
    print("It should be a number")

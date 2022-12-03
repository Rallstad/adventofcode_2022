def read_file(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        num_arr = [line for line in lines]
    return num_arr


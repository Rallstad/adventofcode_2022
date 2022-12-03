# ROCK PAPER SCISSOR
# A for Rock, B for Paper, and C for Scissors - opponent
# X for Rock, Y for Paper, and Z for Scissors - you


def task_a(int_num_arr):
    points = 0
    opponent_shapes = ['A', 'B', 'C']
    your_shapes = ['X', 'Y', 'Z']
    outcomes = {
        'A X': 3,
        'A Y': 6,
        'A Z': 0,
        'B X': 0,
        'B Y': 3,
        'B Z': 6,
        'C X': 6,
        'C Y': 0,
        'C Z': 3,
    }
    points_for_shapes = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    for line in int_num_arr:
        points += outcomes[line]
        opponents_choice = line[0]
        your_choice = line[2]
        points += points_for_shapes[your_choice]

    print("POINTS: ", points)
    return points


def task_b(int_num_arr):
    points = 0
    opponent_shapes = ['A', 'B', 'C']
    points_for_outcome = {'X': 0, 'Y': 3, 'Z': 6}
    points_for_shapes = {'A': 1, 'B': 2, 'C': 3}

    for line in int_num_arr:
        needed_outcome = line[2]
        points += points_for_outcome[needed_outcome]
        opponents_choice = line[0]
        index = opponent_shapes.index(opponents_choice)

        if needed_outcome == 'X':
            index -= 1
            if index == -1:
                index = 2
            your_choice = opponent_shapes[index]
            points += points_for_shapes[your_choice]
        elif needed_outcome == 'Y':
            points += points_for_shapes[opponents_choice]
        elif needed_outcome == 'Z':
            index += 1
            c = index % 3
            your_choice = opponent_shapes[c]
            points += points_for_shapes[your_choice]

    print("POINTS: ", points)
    return points

window_size = (800, 600)
grid_size = (5, 7)
cell_size = (50, 50)


def compare(correct: list, submitted: list):
    ret_list = []
    for i in range(5):
        if correct[i] == submitted[i]:
            ret_list.append(2)
        elif submitted[i] in correct:
            ret_list.append(1)
        else:
            ret_list.append(0)
    return ret_list

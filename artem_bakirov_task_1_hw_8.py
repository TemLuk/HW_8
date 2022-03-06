def max_of_three_ints(*args):
    new_list = list(args)
    max_in_list = max(new_list)
    return max_in_list


print(max_of_three_ints(-6, -15, -2))
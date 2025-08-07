# Problem 4: IndexError
# def get_last_item(my_list):
#     return my_list[len(my_list)]
#
# print(get_last_item([10, 20, 30]))
# Task: Fix the function so it returns the last item of the list without error.

def get_last_item(my_list):
    return my_list[-1]

print(get_last_item([10, 20, 30]))
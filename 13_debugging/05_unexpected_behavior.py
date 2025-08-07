# Problem 5: Unexpected Behavior
# def append_number(num, my_list=[]):
#     my_list.append(num)
#     return my_list
#
# print(append_number(1))
# print(append_number(2))
# print(append_number(3))
# Task: This is supposed to return a fresh list each time. Fix it so it works as expected.

def append_number(num, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(num)
    return my_list

print(append_number(1))
print(append_number(2))
print(append_number(3))
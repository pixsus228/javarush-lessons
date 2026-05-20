# from utils import *

# send_sms()
# send_email()
#
# print(PHONE_NUMBER)
#

# list, set, tuple


# class Iterable:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return Iterator(self.iterable)
#
# class Iterator:
#     def __init__(self, iterator):
#         self.iterator = iterator
#         self.index = 0
#
#     def __next__(self):
#         el = self.iterator[self.index]
#         self.index += 1
#         return el
#
#     def __iter__(self):
#         return self


# class Test:
#     def __init__(self, a):
#         self.a = a
#
#     def __eq__(self, other):
#         return self.a == other.a


class MyList(list):
    def __init__(self, value):
        super().__init__(value)

    def __getitem__(self, index):
        if not isinstance(index, int):
            return None
        if abs(index) >= len(self):
            return None
        return super().__getitem__(index)

    def __setitem__(self, index, value) -> None:
        if index < 0:
            super().insert(index, value)
        elif index >= len(self):
            super().append(value)
        else:
            super().__setitem__(index, value)

# lst = MyList([100, 2, 6, 12])
#
#
# lst[-100] = 123
# lst[100] = 456
# lst[2] = 1010
#
# print(lst)



def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# print(add_to_list("apple"))
# print(add_to_list("banana"))
# print(add_to_list("cherry"))

# 1 спосіб
ages = [15, 18, 12, 52, 23, 62, 24, 19]
new_ages = []
for age in ages:
    if age >= 18:
        new_ages.append(age)

# 2 спосіб
new_ages = [age for age in ages if age >= 18]

# 3 спосіб
new_ages = list(filter(lambda x: x >= 18, ages))


# def create_multipliers():
#     return [lambda x, i=i: i * x for i in range(5)]
#
# for multiplier in create_multipliers():
#     print(multiplier(2))


lst = [1,2,3]

for i in lst:
    print(i)
for i in lst:
    print(i)

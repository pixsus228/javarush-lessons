# file = open("data2.txt", "r+")

# file.write("line 1\n")
# file.write("line 2\n")
# file.write("line 3\n")

# lines_len = len(file.readlines())
#
# file.writelines([f"line {i}\n" for i in range(lines_len+1, lines_len+4)])
#
# file.close()


# line = file.readline()
# while line:
#     line = file.readline()
#
#     print(line.strip())
#
#
# file.close()


# with open("example.bin", "wb") as file:
#     file.write(b'hello')
#
# with open("example.bin", "rb") as file:
#     line = 12
#     print(file.read())
#

import os
import shutil

def create_files(dest: str, amount: int):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for i in range(1, amount+1):
        with open(f"{dest}/{str(i)}.txt", "w") as file:
            file.write(str(i))


# create_files("data", 100)


import pickle

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_minor(self):
        return self.age < 18


# with open("obj.pkl", "wb") as file:
#     pickle.dump(User("Bob", 25), file)

with open("obj.pkl", "rb") as file:
    user = pickle.load(file)


print(user)
print(user.age)
print(user.is_minor())

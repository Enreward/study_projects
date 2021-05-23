#!E:\Учёба\Программирование\Python\Курс Stepic\tests\venv\Scripts python
# -*- coding: utf-8 -*-

def read_file(path):
    with open(path, "r") as f:
        data = f.readlines()
    return data

def write_file(path, data):
    with open(path, "w") as f:
        for d in data:
            f.write(d + "\n")
    return 0

if __name__ == "__main__":
    data = read_file("dataset_average_score.txt")
    write_file("text.txt", data)

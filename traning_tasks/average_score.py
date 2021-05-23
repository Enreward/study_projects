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

def average_score(data):
    mark = []   # здесь временно хранятся оценки
    list_students = {}  # солварь студентов и их оценок
    for d in data:
        temp = d.strip().split(';')
        for j in range(1, len(temp)):
            mark.append(temp[j])
        list_students[temp[0]] = mark
        mark = []

    students_average_score = []                             # средний балл по студенту
    subject_average_score = [0 for i in range(len(temp)-1)]      # средний балл по предметам
    average = 0
    for student in list_students:
        for i in range(len(list_students[student])):
            current = int(list_students[student][i])
            average += current
            subject_average_score[i] += current
        students_average_score.append(str(average / len(list_students[student])))
        average = 0

    result = ''
    for i in range(len(subject_average_score)):
        subject_average_score[i] /= len(list_students)
        result += str(subject_average_score[i]) + ' '

    students_average_score.append(result)
    return students_average_score

if __name__ == "__main__":
    data = read_file("dataset_average_score.txt")
    data = average_score(data)
    write_file("average score.txt", data)

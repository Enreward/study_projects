# coding: utf-8

import requests

def read_file(path_to_file):
    data = []
    with open(path_to_file, 'r') as file:
        for s in file.readlines():
            data.append(s.strip())
    return data

def write_file(path, data):
    with open(path, 'w') as file:
        file.write(str(data) + "\n")

if __name__ == '__main__':
    url = read_file("dataset_achivement.txt")[0]
    base = (url[0:url.rindex('/')+1])
    response = requests.get(url).text
    print("Processing..")
    while response.find("We") == -1:
        response = requests.get(base + response).text
    write_file("Achievement.txt", response)

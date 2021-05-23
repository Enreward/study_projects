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
    urls = read_file("dataset_request.txt")
    response = []
    for url in urls:
        response.append(requests.get(url))

    for r in response:
        txt = r.text
        txt = txt.splitlines()
        write_file("requests.txt", len(txt))

import os
import sys

ROOT_PATH = os.path.dirname(sys.argv[0])
DATA_PATH = os.path.join(ROOT_PATH, 'data_for_task_2.4.1')
if __name__ == '__main__':
    with open(os.path.join(DATA_PATH, 'dataset_24465_4.txt')) as f:
        text_lines = f.readlines()

    with open(os.path.join(DATA_PATH, 'output.txt'), 'w') as f:
        f.writelines(text_lines[::-1])

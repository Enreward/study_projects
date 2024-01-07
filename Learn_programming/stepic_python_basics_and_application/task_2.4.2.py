import os
import sys
import zipfile


ROOT_PATH = os.path.dirname(sys.argv[0])
DATA_PATH = os.path.join(ROOT_PATH, 'data_for_task_2.4.2')

if __name__ == '__main__':
    archive_name = 'main.zip'
    folder_name = archive_name.split('.')[0]
    result_list = []

    with zipfile.ZipFile(os.path.join(DATA_PATH, archive_name), 'r') as zip_file:
        zip_file.extractall(os.path.join(DATA_PATH, folder_name))

    i = len(os.path.join(DATA_PATH, folder_name))
    basename = os.listdir(os.path.join(DATA_PATH, folder_name))[0]
    for cur_dir, inner_dirs, files in os.walk(os.path.join(DATA_PATH, folder_name, basename)):
        cur_dir = cur_dir[i + 1:]
        for file in files:
            if os.path.splitext(file)[1] == '.py' and cur_dir not in result_list:
                result_list.append(cur_dir)

    result_list.sort()

    with open(os.path.join(DATA_PATH, 'output.txt'), 'w') as f:
        f.write('\n'.join(result_list))

#!/usr/bin/env python3
# Author ID: 111116240

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data


def read_file_list(file_name):
    f = open(file_name, 'r')
    data = f.readlines()
    f.close()

    clean_list = []

    for line in data:
        clean_list.append(line.strip('\n'))

    return clean_list


if __name__ == '__main__':
    file_name = 'data.txt'

    print(read_file_string(file_name))
    print(read_file_list(file_name))
import re
import sys
import os


def decode(message_file):
    file = open(message_file, "r")
    dict = {}
    for line in file:
        num = re.search("^[0-9]+", line)[0]
        word = re.search("^[0-9]+ (.+)", line)[1]
        dict[num] = word
    n = 1
    i = 2
    output = ''
    while n <= len(dict):
        output += "{} ".format(dict[str(n)])
        n += i
        i += 1
    return output


def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if (os.path.isfile(file_name)):
            print(decode(file_name))
        else:
            print('file not found')

    else:
        print('what you wan me do?')


if __name__ == '__main__':
    main()

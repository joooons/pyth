import sys
import re

def main():
    print('')

    if len(sys.argv) < 2:
        print('Please specify a command: [create] || [find]')
        print('')
        return 0
    
    if sys.argv[1] == 'create':
        if (len(sys.argv) < 3):
            print('[create] :: what is the name of the file you would like to create?')
        elif (len(sys.argv) < 4):
            print('[create] :: what would you like to write in [{}.txt]?'.format(sys.argv[2]))
        else:
            filename = "{}.txt".format(sys.argv[2])
            content = ''
            for i in range(3, len(sys.argv)):
                content += sys.argv[i] + ' '
            with open(filename, "w") as file:
                file.write(content)
                print('Successfully wrote some stuff into {}'.format(filename))
    
    if sys.argv[1] == 'find':
        if (len(sys.argv) < 3):
            print('[find] :: what file do you want to read?')
        else:
            filename = "{}.txt".format(sys.argv[2])
            with open(filename, "r") as file:
                str = file.read()
                print("[{}] says this: {}".format(filename, str))

    if sys.argv[1] == 'analyze':
            if (len(sys.argv) < 3):
                print('[analyze] :: what file do you want to analyze?')
            else:
                filename = "{}.txt".format(sys.argv[2])
                with open(filename, "r") as file:
                    str = file.read()
                    print("[{}] says this: {}".format(filename, str))
    
    if re.match("(?!^create$|^find$|^analyze$)", sys.argv[1]):
        print('Please specify a command: [create] || [find]')

    
    
    print('')
    


if __name__ == '__main__':
    main()
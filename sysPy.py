import sys

def main():
    print('')
    if len(sys.argv) < 2:
        print('please enter a command next time. Try something like \'create\'')
        return 0
    if sys.argv[1] == 'create':
        if (len(sys.argv) < 3):
            print('what should I create? Please specify next time.')
        else:
            with open("output.text", "w") as file:
                file.write('what is this thing?')
                
        return 0
    else:
        print('length of list of arguments is', len(sys.argv))
    


if __name__ == '__main__':
    main()


def main():
    print('\n\nWelcome to the OS MODULE HELP TOOL Developed by BLACK CODERS\n\n') 
    while True:
        know = input('''
1. To know what os.system is.....
2. Format
3. How to install any library with pip function using os.system module
4. How to execute linux command in terminal using os module
5. Documentation for os.system module
6. Exit

Your Choice :- ''')
        if know == '1':
            print('\n\nThe OS module in Python provides functions for interacting with the operating system. OS comes under Python\'s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os. path* modules include many functions to interact with the file system.\n\n')

        elif know == '2':
            print('\n\nos.system(\'any command\')')
            print('Example :- os.system(\'apt-get update\')\n\n')

        elif know == '3':
            print('\n\nExample :- os.system(\'pip3 install pytube (any libraries)\')\n\n')

        elif know == '4':
            print('\n\nos.system(\'any_command\')')
            print('Example : os.system(\'apt-get install python\')\n\n')

        elif know == '5':
            print('\n\nWebsite for Documentation : https://docs.python.org/3/library/os.html\n\n')

        elif know == '6':
            print('\n\nThanks for Using Tool\n\n')
            break

        else:
            print('\n\nEnter valid Input\n\n')

main()
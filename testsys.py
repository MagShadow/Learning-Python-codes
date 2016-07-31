# test sys module

import sys

def readfile(filename):
    '''Print a file to standard output'''
    f=open(filename)
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end='')
    f.close()

if len(sys.argv)<2:
    print("No Action!")
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    if option=='version':
        print("Version 1.2")
    elif option=='help':
        print('''No help here!
go die!
Bye~''')
    else:
        print('Unknown')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)

#Taimur Shaikh
#ASCII to RLE compression

from os import path ##path command from os library

def EnterRLE():
    x = False
    lines = []##List of lines

    while not x:
        try: ##try and except loops to handle if the user enters letters
            line_count = int(input('Enter the amount of lines your RLE is '))
            while line_count <2: ##If input is less than 2
                line_count = int(input('Invalid. Must be greater than 2 '))

        except ValueError:
            print("Invalid")
            continue
        x = True
    for i in range(line_count):
        line = input('Enter RLE of Line ' + str(i+ 1)+' ') ##User enters current line of RLE
        while len(line) == 0 or len(line) % 3 != 0: ##If line is blank or its length is not divisible by 3, it can't be decompressed
             line = input('Invalid entry. Enter RLE of Line ' + str(i+ 1)+' ')
        lines.append(line)
    for line in lines: ##Line by line decompression
        res = ''
        for i in range(0,len(line),3): ##i goes up in 3s
            char = line[i:i+3] ##Making a chunk of the current line with length of 3, corresponding to RLE code of one character eg. '01e' or '23r'
            if char[0] == '0': ##If chunks number segment is one digit
                res += (char[-1]*(int(char[1])))
            else:
                res += (char[-1]*(int(char[:2])))
        print(res)
    return ' '
def DisplayASCIIArt():
    x = input('Enter name of file containing ASCII art ')
    while not (path.exists(x)): ##Using path to check if file name inputted exists within the same folder as this code
        x = input('File not found. Please enter valid file name ')
    f = open(x,'r') ##Opened in read mode
    string = f.read() ##Creating an object with a string of the file's contents
    f.close()##Closing file (good practice)
    return ('\n'+string)


def ConvertToASCIIArt():
    x = input('Enter name of file containing RLE code ')

    while not (path.exists(x)):
        x = input('File not found. Please enter valid file name ')
    f = open(x,'r')

    string = f.read()

    f.close()
    string = string.split('\n') ##Turning string into a LIST, where every element is a line from the RLE file
    for line in string:
        if len(line) % 3 != 0:
            print('This file is not valid.')
            return ' '
        res = '' ##String which will be returned
        for i in range(0,len(line),3):
            char = line[i:i+3]


            if char[0] == '0':
                res += (char[-1]*(int(char[1])))
            else:
                try:

                    res += (char[-1]*(int(char[:2])))
                except ValueError: ##Exception to handle the error if there is a character which cannot be converted to an integer
                                    # E.g: in '1fr', 'f' should be an integer
                    print('This file is not valid RLE')
                    return' '
        print(res) ##Every line is outputted indivdually, and res is turned back into a blank string
    return ' '



def ConvertToRLE():
    x = input('Enter name of file containing ASCII art ')
    while not (path.exists(x)):
        x = input('File not found. Please enter valid file name ')
    f = open(x,'r')
    string = f.read()

    art_lst = string.splitlines() ##Using a list to calculate length of art (minus newlines)
    art_len = sum([len(x) for x in art_lst])
    print('Art Length:' + str(art_len))
    f.close()
    prev_char = string[0]
    count = 0
    res = []
    for char in string:

        if char == prev_char: ##If the character is the same as the last one, continue
            count += 1
            prev_char = char ##Current character is now the new previous one

        else:
            if len(str(count)) > 1: ##If count isn't  a one digit number
                res.append(str(count)+ prev_char) ##Add the string version of count to the list along with last character
                prev_char = char ##Making current char now the last char
                count = 1 ##Resetting count

            else:
                res.append('0' + str(count)+ prev_char) ##Same thing except with 0 at the beginning
                prev_char = char
                count =1
        if char == '\n':
           res.append(char)
           continue
    if string[-1] != string[-2] and string[-1] : ##My algorithm doesnt reach the last character if it is unique, so these 2 lines are needed
        res.append('01' + string[-1])

    else:
        res.append(char)
    res = ''.join(res)

    res = [x for x in res.splitlines()[::2]]
    res_len = sum([len(x) for x in res])
    res = ''.join([x + '\n' for x in res]) ##These lines make sure the length does not take into account newlines

    print('RLE length:' + str(res_len))
    f2 = open('Compressed.txt','w+') ##Makes a new file in write mode
    f2.write(res)
    f2.close()##Writes RLE to new file
    return 'New file created. Check directory\n' + str(art_len - res_len) + ' characters saved' ##displays character difference



def Menu():
    choice = (input('\nSelect one of the following:\n1) Enter RLE\n2) Display ASCII art\n3) Convert to ASCII art\n4) Convert to RLE\n5) Quit '))

    if choice == '1':
        print (EnterRLE())
        Menu() ##Menu function recursively called after every function
    if choice == '2':
        print(DisplayASCIIArt())
        Menu()

    if choice == '3':
        print(ConvertToASCIIArt())
        Menu()

    if choice == '4':
        print(ConvertToRLE())
        Menu()

    if choice == '5':
        print('Goodbye')
        quit()
    else:
        print('Invalid input')
        Menu()






Menu()

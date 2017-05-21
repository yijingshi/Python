student = 12
namelist = []
namelist_tuple = []

def main():
#namelist_2 = []
    get_name()
    print namelist

#sortlist
    sort_list ()
    print('Sorted namelist: ', namelist)

#reverselist
    reverse_sort_list ()
    print('Reversed namelist: ', namelist)

#ask for instructor's name
    instr_name()
    print namelist

#insert my name
    my_name()
    print('The list after insert: ', namelist)

#open a file for writing
    write_file ()

# convert list to tuple

    convert_tuple ()


def get_name():
    for name in range (student):
        name = name +1
        name = raw_input("Enter the name: ")
        namelist.append(name)

def sort_list():
    namelist.sort()

def reverse_sort_list():
    namelist.reverse()

def instr_name():
    instr_name1 = raw_input("Enter the instructor's name: ")
    namelist.append(instr_name1)

def my_name():
    myname = raw_input("Enter your name: ")
    namelist.insert(0, myname )

def write_file():
    outfile = open ('names.txt','w')
    for name in namelist:
        outfile.writelines(name +'\n')
    outfile.close()


def convert_tuple ():
    namelist_tuple = tuple(namelist)
    print ('Converted to tuple: ', namelist_tuple)
main()

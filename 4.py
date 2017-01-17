
gradefile = open('grades.txt','w')
def main():

    i = 0
    while i<3:
        name = raw_input ("enter your name: ")
        ave_grade = input ("enter the average grade: ")
        try:
            if ave_grade > 0 and ave_grade < 100:
                gradefile.write(name + '\n')
                gradefile.write(str(ave_grade) + '\n')
                i = i+1
            else:
                print ("Error: grade has to be between 0-100, Please re-enter")
        except ValueError:
            print("Error: grade has to be between 0-100, Please re-enter")

main()
gradefile.close()

def display():
    try:

        infile = open ('grades.txt', 'r')
        contents = infile.read()
        print(contents)
        infile.close()


    except IOError:
        print ('An error occured trying to read file')


display()

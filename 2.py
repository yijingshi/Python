i=0
grade = 0
total = 0



while grade != -1:
    grade = int(input("type a grade: "))
    #total = total + grade
    if grade >= 90:
        print ("Your grade is A")
        #i=i+1
    if 80 <= grade < 90:
        print ("Your grade is B")
        #i=i+1
    if 70 <= grade < 80:
        print ("Your grade is C")
        #i=i+1

    if 60 <= grade < 70:
        print ("Your grade is D")
        #i=i+1

    else:
        print ("You made an F! Obviously you did not study!")
    i=i+1
    total = total + grade
    print "enter times: ",i-1
    #total = total + grade
    print 'total is: ',total+1
    average = (total/ i)+1
    print 'average is: ', average

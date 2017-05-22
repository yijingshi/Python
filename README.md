# sales-calculation-1
python practice/hw

Write a complete and syntactically correct Python program to solve the following problem: You are the payroll manager for SoftwarePirates Inc. You have been charged with writing a package that calculates the monthly paycheck for the salespeople. Salespeople at SoftwarePirates get paid a base salary of $2000 per month. Beyond the base salary, each salesperson earns commission on the following scale:
Sales  <$10000 Commission Rate 0 Bonus 0
Sales  $10000 – $100,000 Commission Rate 2% Bonus 0
Sales  $100,001 - $500,000 Commission Rate 15% Bonus $1000
Sales  $500,001 - $1,000,000 Commission Rate 28% Bonus $5000
Sales  >$1,000,000 Commission Rate 35% Bonus $100,000

1. The following additional conditions apply:
2. If a salesperson has taken more than 3 vacation days in a month, their pay gets reduced
by $200
3. A salesperson earns a bonus only if they have been with the company for 3 months or
more
4. For salespeople who have been with the company for 5 years or more and who have
made sales greater than $100,000 an additional bonus of $1000 is added.
All input to the program will be interactive from the keyboard. The output of the program will include:
a. The name of the salesperson
b. Their longevity with the company
c. Their base salary
d. The commission earned (in Dollars)
e. The bonus earned
f. Additional bonus earned (if any)
g. Deductions (if any)
h. A total gross paycheck
i. Your output should look like a paystub (NOT in paragraph format)
j. All currency should be formatted with a $ sign and 2 decimal places.

#student-Grades-Calcuation-2
Write a complete and syntactically correct Python program to solve the following problem:
You are the professor for COSC 1336 at Austin Community College. You want to write a program that will take in the numeric grades of the students in your class. Since the students in a class vary from semester to semester, there is no fixed number assigned to the number of students. You will keep track of how many students’ grades you input. You will stop taking input when the student enters a grade of -1.
Your program will use loops and will accomplish the following:
1. Read in a numeric grade from a student.
2. Convert the numeric grade to a letter grade using the grade policies in your syllabus.
3. Keep a running total of the numeric grades entered.
4. Keep a count of the number of grades entered.
5. Issue a message that comments on the letter grade earned. As an example, you may
write “You made an F! Obviously you did not study!”
6. At the end the program will calculate a class average unless there were no grades
entered.
All input to the program will be interactive from the keyboard. The output of the program will include the individual grades converted, the message issued to the student, a class average, and the number of grades entered.

#Guess a number - 3
Write a complete and syntactically correct Python program to solve the following problem: Write a simple guessing game using the following specs:
1. Generate a random number between 1 and 1000.
2. Ask the player to guess the number. You will keep track of the number of guesses.
3. If the player’s guess is higher than the number generated then display the message “Too
High!” If the player’s guess is within a 10-point difference of the number generated but
higher than the number generated, then give the message “Getting warm but still high!”
4. If the player’s guess is lower than the number generated then display the message “Too
Low!” If the player’s guess is within a 10 point difference of the number generated but lower than the number generated, then give the message “Getting warm but still Low!”

5. The program will keep taking guesses until the player guesses the number.
6. Once the player guesses the number, give them a congratulatory message like “You rock!
You guessed the number in x tries!!” where x is the actual number of tries it took the player to guess the number. You can write any message as long as you include the number of tries in the message.
7. Once the player has guessed the number, ask them if they wish to play again. If they do then generate another random number and start the game over again.
8. All input to the program will be interactive from the keyboard.

#Files and Exception -4
Write a program for Professor at College that allows him to keep a record of the students’ average grade in his class. The program must be written in accordance with the following specs:
1. The input must be interactive from the keyboard. You will take input for 12 students.
2. You will input the students’ name and an average grade. The student cannot enter
an average below zero or above 100. Your program must raise and handle an exception should this occur.
a. The exception should cause the program to return and get a new grade
3. Write all out put to a file named grades.txt
4. Close the out put file.
5. Open the file grades.txt for input.
6. Your program will raise and handle an exception if the file is not found.
a. I will test this aspect by changing the filename and looking for your exception code (your exception should cause program to ask for correct file name).
7. Read all the records from the file and display them.

#list -7

Write a program for Professor at College that allows him to read in student names. The program must be written in accordance with the following specs:
1. You must use functions and pass the list in and out of the function.
2. The input must be interactive from the keyboard. You will take input for 12 students.
3. You will input the students’ name and insert/append each name in a list named
students.
4. Sort the list in alphabetical order.
5. Sort the list again in reverse order.
6. Append the instructor’s name on to the list.
7. Insert your own name at the beginning of the list.
8. Write the list to a file.
9. Displaythecontentsofthefilenamednames.txt.
10.Convert the list to a Tuple.


#string -6
1. Input a date in numeric format from the user e.g. mm/dd/yy.
2. Examine the month entered by the user. If it is larger than 12 or smaller than 1
issue an error message and ask for input again.
3. Perform similar validation tests for the date and year. Year must be 2013. (Any
other year is invalid) In addition, the year must only be two digits long.
4. Once all input has been validated, output the string in long date format. Thus a string that was input as 06/01/15 will be output as June 1, 2015.

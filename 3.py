import random
guess = 0
def main():
    number = random.randint(1,1000)
    i=0
    guess_it = guess_again()
    while guess_it != number:
        if guess_it > number +11:
            print "Too High!"
            guess_it = guess_again()
            i= i+1
        elif number +11 > guess_it > number:
            print "Getting warm but still high!"
            guess_it = guess_again()
            i= i+1
        elif number -11 < guess_it < number:
            print "Getting warm but still low!"
            guess_it = guess_again()
            i= i+1
        elif guess_it < number -11:
            print "Too low!"
            guess_it = guess_again()
            i= i+1
    else:
        print "You rock!You guessed the number in", i, "tries!!"
        again = raw_input("Do you want to try agian? y for play again")
        if again == 'y':
            return main()

def guess_again():
    guess = int(input("Guess a number!"))
    print ("The number you guessed is: ", guess)
    return guess

main()

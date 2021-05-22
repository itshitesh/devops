print("Welcome to an odd-even game!")
def Game(): 
    print("what number are you thinking of between 1 and 1000?")
    while True:
        try:
            guess = int(input("Guess the number: "))
            num = (guess%2)
        except ValueError:
            print("Sorry I did not understand")
            continue
        if num == 0:
            print("You have entered even number")
            print("Please enter odd numer to break the program")
            continue
        else:
            print("You have entered odd number")
            break
Game()
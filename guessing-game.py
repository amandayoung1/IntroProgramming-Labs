def main():
    print ("PYTHON GUESSING GAME.")
    animal = "dog"
    while True:
        print ("I am thinking of an animal.")
        guess = input("Guess what animal I am thinking of: ")
        guess = guess.lower()
        if guess == animal:
            print ("Congratulations! You guessed it!")
            break
        else:
            print ("Sorry! Try again...")
            
        

main()

def main():
    print ("PYTHON GUESSING GAME.")
    animal = "dog"
    while True:
        print ("I am thinking of an animal.")
        guess = input("Guess what animal I am thinking of: ")
        guess = guess.lower()
        if guess[0] == "q":
            print("Thanks for playing. Bye!")
            break
        elif guess == animal:
            print ("Congratulations! You guessed it!")
            response = input("Do you like this animal? State y for yes or n for no.\n")
            response = response.lower()
            if response == "y":
                print("Cool! I like dogs also.")
            else:
                print ("Aw, sorry to hear that.")
            break
        else:
            print ("Sorry! Try again...")
            
            
        

main()

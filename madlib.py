# Intro to Programming
# Author: Amanda Young
# Date: 9/13/2018
# Mad Lib Program for Lab Exercise

def promptForWords(): 
    global noun, verb, adjective, place
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    print("\n")

def makeAndPrintSentence():
    print("Grab the " + adjective + " " + noun + " and " + verb + " to the " + place + ".")
    
def main():
    promptForWords()
    makeAndPrintSentence()

main()

    
    

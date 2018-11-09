# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Amanda Young
# Created: 11-08-2018

symbol = [ " ", "x", "o" ]
global matrix
matrix = [ [" "," "," "],
               [" "," "," "],
               [" "," "," "] ]


def printRow(row):
    global matrix
    matrix = [ [" "," "," "],
               [" "," "," "],
               [" "," "," "] ]


def printBoard():
    print("+-----------+\n"
          "| " +matrix[0][0]+ " | " +matrix[0][1]+ " | " +matrix[0][2]+ " |\n"
          "+-----------+\n"
          "| " +matrix[1][0]+ " | " +matrix[1][1]+ " | " +matrix[1][2]+ " |\n"
          "+-----------+\n"
          "| " +matrix[2][0]+ " | " +matrix[2][1]+ " | " +matrix[2][2]+ " |\n"
          "+-----------+\n")
    
def markBoard():
    global player
    column = input("Which column would you like to make your move in? ").strip()
    row = input("Which row would you like to make your move in? ").strip()
    if column == "1":
        if row == "1":
            if player == 1:
                if matrix[0][0] == " ":
                    matrix[0][0]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[0][0] == " ":
                    matrix[0][0]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row =="2":
            if player == 1:
                if matrix[1][0] == " ":
                    matrix[1][0]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[1][0] == " ":
                    matrix[1][0]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row == "3":
            if player == 1:
                if matrix[2][0] == " ":
                    matrix[2][0]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[2][0] == " ":
                    matrix[2][0]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
    elif column == "2":
        if row == "1":
            if player == 1:
                if matrix[0][1] == " ":
                    matrix[0][1]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[0][1] == " ":
                    matrix[0][1]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row =="2":
            if player == 1:
                if matrix[1][1] == " ":
                    matrix[1][1]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[1][1] == " ":
                    matrix[1][1]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row == "3":
            if player == 1:
                if matrix[2][1] == " ":
                    matrix[2][1]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[2][1] == " ":
                    matrix[2][1]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
    elif column == "3":
        if row == "1":
            if player == 1:
                if matrix[0][2] == " ":
                    matrix[0][2]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[0][2] == " ":
                    matrix[0][2]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row =="2":
            if player == 1:
                if matrix[1][2] == " ":
                    matrix[1][2]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[1][2] == " ":
                    matrix[1][2]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
        elif row == "3":
            if player == 1:
                if matrix[2][2] == " ":
                    matrix[2][2]= "x"
                else:
                    print("Sorry, that spot has already been marked!")
            if player == 2:
                if matrix[2][2] == " ":
                    matrix[2][2]= "o"
                else:
                    print("Sorry, that spot has already been marked!")
    else:
        print("Sorry, that is not a valid location. Try again!")

    
def getPlayerMove():
    global row, column, player
    column = input("Which column would you like to make your move in? ").strip()
    row = input("Which row would you like to make your move in? ").strip()


def hasBlanks():
    if matrix [0][0] == " ":
        return True
    elif matrix [0][1] == " ":
        return True
    elif matrix [0][2] == " ":
        return True
    elif matrix [1][0] == " ":
        return True
    elif matrix [1][1] == " ":
        return True
    elif matrix [1][2] == " ":
        return True
    elif matrix [2][0] == " ":
        return True
    elif matrix [2][1] == " ":
        return True
    elif matrix [2][2] == " ":
        return True
    else:
        return False
    

player = 1

def main():
    global player
    while hasBlanks():
        player = player % 2 + 1 
        markBoard()
        printBoard()
    print ("Game over! Thanks for playing!")
    
    
        
main()

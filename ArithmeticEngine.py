# CMPT 120 - Lab #6
# Amanda Young
# 10-25-2018
###
def showIntro():
 print("Welcome to the Arithmetic Engine!")
 print("=================================\n")
 print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
 
def showOutro():
 print("\nThank you for using the Arithmetic Engine…")
 print("\nPlease come back again soon!")
 
def doLoop():
    global result
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
       
        if cmd == "add":
            getInput()
            result = num1 + num2
            printResult()
        elif cmd == "sub":
            getInput()
            result = num1 - num2
            printResult()
        elif cmd == "mult":
            getInput()
            result = num1 * num2
            printResult()
        elif cmd == "div":
            getInput()
            result = num1 // num2
            printResult()
        elif cmd == "quit":
            break
        else:
            print(cmd + " is not a valid command.\n")
            
def printResult():
    global result
    print("The result is " + str(result) + ".\n")

def getInput():
    global num1, num2
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
def main():
 showIntro()
 doLoop()
 showOutro()
main()

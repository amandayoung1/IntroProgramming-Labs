# Amanda Young
# CMPT 120
# Lab 4
# 9/20/18
# Fibonacci -- Chap 3 Programming Exercise #16

def text():
    print("Hello!"
          "\n======"
          "\nThis program computes the nth Fibonacci number. \n")
    
def calc():
    
    global n, previous, beforePrevious, result
    n = int(input("Enter the nth number: "))

    previous, beforePrevious = 1, 1

    for i in range (n-2):
        result = previous + beforePrevious 
        previous, beforePrevious = result, previous

def end():
    print("\nThe " + str(n) + "th Fibonacci number is " + str(result) + ".")
    

def main():
    text()
    calc()
    end()

main()

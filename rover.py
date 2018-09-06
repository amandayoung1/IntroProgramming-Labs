# CMPT 120L 113
# Mars Rover Program
# Author: Amanda Young
# Created: 6 Sep 2018

#Light travels at 186000 miles per second
#Mars and NASA are at a distance of about 34 million miles 
def main():
    print("This program calculates how long it takes a photo from Curiosity to reach NASA when Mars is at its closet orbit to Earth.")
    speed= 186000
    distance= 34000000
    traveltime= distance/speed
    print("The travel time is ", traveltime, "seconds.")
    
main()


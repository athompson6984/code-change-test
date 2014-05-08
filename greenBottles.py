#10 Green Bottles challenge
import time #Import time for pauses
bottles =10 #Create the counting variable
while bottles > 0: #Start a loop that will print the rhyme and count down to 0
    print("\n"bottles, " green bottles, sitting on the wall")
    time.sleep(2)
    print(bottles, " green bottles, sitting on the wall")
    time.sleep(2)
    print("And if 1 green bottle should accidentally fall,")
    time.sleep(2)
    bottles = bottles-1 #Count down
    print("There'll be ", bottles, " green bottles, sitting on the wall.")
    time.sleep(3)

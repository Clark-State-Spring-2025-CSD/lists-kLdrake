#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

random.seed()

PlayerOne = []

PlayerTwo = []

for i in range(10):
    PlayerOne.append(random.randint(1,50))
    PlayerTwo.append(random.randint(1,50))

print("Player One = ",(PlayerOne))
print("Player Two = ",(PlayerTwo))

sum1 = []

for p1, p2 in zip(PlayerOne, PlayerTwo):
    if p1 > p2:
        sum1.append(1)
    elif p1 < p2:
        sum1.append(2)

print("Player One Won ",sum1.count(1)," times")
print("Player Two Won ",sum1.count(2)," times")

high1 = max(PlayerOne)
high2 = max(PlayerTwo)

hi1 = PlayerOne.index(high1) + 1
hi2 = PlayerTwo.index(high2) + 1

print("Player One's highest number is" ,high1, "at index" ,hi1)
print("Player Two's highest number is" ,high2, "at index" ,hi2)

low1 = min(PlayerOne)
low2 = min(PlayerTwo)

lo1 = PlayerOne.index(low1) + 1
lo2 = PlayerTwo.index(low2) + 1

print("Player One's lowest number is" ,low1, "at index" ,lo1)
print("Player Two's lowest number is" ,low2, "at index" ,lo2)
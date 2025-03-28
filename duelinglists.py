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

player1 = []
player2 = []
win1 = 0
win2 = 0
draw = 0

for i in range(10):
    player1.append(random.randint(1, 50))
    player2.append(random.randint(1, 50))
print(player1)
print(player2)



for x in range(len(player1)):
    if player1[x] > player2[x]:
        win1 += 1
    if player1[x] < player2[x]:
        win2 += 1
    if player1[x] == player2[x]:
        draw += 1

print(f"Player one won {win1} times.")
print(f"Player two won {win2} times.")
print(f"I was a draw {draw} times.")

playerOneMax = 0
playerTwoMax = 0
playerOneMin = 50
playerTwoMin = 50

for o in player1:
    if o > playerOneMax:
        playerOneMax = o

for o in player2:
    if o > playerTwoMax:
        playerTwoMax = o

for o in player1:
    if o < playerOneMin:
        playerOneMin = o

for o in player2:
    if o < playerTwoMin:
        playerTwoMin = o

print(f"Player one's highest number is {playerOneMax} at index {player1.index(playerOneMax)}")
print(f"Player two's highest number is {playerTwoMax} at index {player2.index(playerTwoMax)}")
print(f"Player one's lowest number is {playerOneMin} at index {player1.index(playerOneMin)}")
print(f"Player two's lowest number is {playerTwoMin} at index {player2.index(playerTwoMin)}")
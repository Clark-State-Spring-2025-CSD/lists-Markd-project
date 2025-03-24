#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#You must use a list for this assignment. Not using a list will result in an automatic 0.
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#[pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken] 
#You entered a total of 62 characters

list = []
characterCount = 0

for x in range(5):
    list.append(str(input("Please enter five food items.")))
for str in list:
    characterCount += len(str)

print(f"Your enter foods are as followed: {list}")
print(f"You entered a total of {characterCount} characters.")
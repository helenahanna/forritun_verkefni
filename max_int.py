#Find the highest positive integer by a user
#Repetedly promt the user for an integer
#Compare the previous input to the current input
#Keep the higher of the two inputs
#Stop when user inputs a negative integer
#Print out maximum integer

num_int = int(input("Input a number: "))
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
 
print("The maximum is", max_int) 

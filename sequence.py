#Sum of first three gives the fourth number
#Sum of second three then gives the fifht number and so forth
#Store the sum of the previous 3 numbers
#Add the sum to the outcome


n = int(input("Enter the length of the sequence: "))
count = 0
sum_int = 3

while count <= sum_int:
        count += 1
    else: 
        count = sum_int + count-1

print(count)


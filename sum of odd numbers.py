# Python Program to Calculate Sum of Odd Numbers from 1 to 20
 
maxnum = 20
oddadd = 0

for num in range(1, maxnum + 1):
    if num % 2 != 0:
        #print("odd number :",num)
        oddadd=oddadd+num
        
print("Sum of Odd Number from 1 to 20 is:",oddadd)

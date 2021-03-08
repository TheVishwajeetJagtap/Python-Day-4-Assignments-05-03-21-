#wirte a program to read number from keyboard and print it in reverse

number=input("Enter the number") 

reverse=0
for i in range(len(number)):
    reminder = int(number) % 10
    reverse = (reverse * 10) + reminder
    number = int(number) / 10
print(reverse)


#********************************using slice******************************************************
num=input("enter any number:")
print(num[::-1])


#********************************using while loop**************************************************
num=int(input("enter any number:"))
rev=0
while(num>0):
    reminder=num%10
    rev=(rev*10)+reminder
    num=num//10
print("reverse number is :",rev)

#********************************using reversed sunction********************************************
num=input("enter any number:") 
for n in reversed(num):
    print(n,end='')
    

#********************************using len********************************************
num=input("enter any number:") 
rev = ''
for i in range(len(num), 0, -1):
    rev += num[i-1]
print(int(rev))

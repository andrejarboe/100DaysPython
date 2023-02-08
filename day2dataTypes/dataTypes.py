# print (len(1235)) type error
# data types

num_char = len(input("What is your name?"))

print(type(num_char))

int_num = str(num_char)

print(type(int_num))

print("your name has " + int_num + " characters")

# Exercise:
# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, 
# then the output should be 3 + 5 = 8

userNum = input("Type a 2 digit number: ")

num1 = int(userNum[0])
num2 = int(userNum[1])

print(num1 + num2)
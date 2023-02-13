# if condition:
#     do this
# else:
#     do this

water_level = 50

if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("welcome to the rollercoaster!")
height = int(input("what is you height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you need to grow taller before you can ride.")

# modulo %
# 7 % 2
# 2 + 2 +2 + 1
# = 1
# 7 % 4
# 4 + 3 
# = 3
print(7 % 4) # 3


height = int(input("how tall are you? "))
bill = 0

if height >= 120:
    print("can ride")
    age =int(input("how old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        print("youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("do you want a photo? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill +=3 

    print(f"Your final bill is ${bill}")

else:
    print("you can not ride")
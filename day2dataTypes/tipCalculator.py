#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What % tip would you like to give? "))
number_of_people = int(input("How many people to split the bill? "))

tip_percent = tip_percent / 100 * bill
bill_total = bill + tip_percent
per_person = round(bill_total / number_of_people, 2)
per_person = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person}")
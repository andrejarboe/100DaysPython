# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)


days = 365
weeks = 52
months = 12

years_left = 90 - age
days_left = years_left * days
weeks_left = years_left * weeks
months_left = years_left * months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
# Wayne Swamber Jr
# PSID: 1419882
# Calculate the age of person based on current date and the birthday of the user.
# The program should:
# Prompt the user to enter the current date by month, day and year
# Prompt the user to enter the birthday by month, day and year
# Output the age of the user in years
# Output a "Happy Birthday!" message if the current date is the user's actual birthday.

print("Birthday Calculator")
print("Current day")

cd_month = int(input("Month: "))
cd_day = int(input("Day: "))
cd_year = int(input("Year: "))

print("Birthday")

bd_month = int(input("Month: "))
bd_day = int(input("Day: "))
bd_year = int(input("Year: "))

if cd_month == bd_month and cd_day == bd_day:
    print("Happy Birthday!")

age = cd_year - bd_year

print("You are", age, "years old.")







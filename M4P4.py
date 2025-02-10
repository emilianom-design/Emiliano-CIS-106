# Input
Name = input("enter first name")
Steps = float(input("number of steps walked in a day"))

# Process
Daily_calories_burned = (Steps * .25)

# Output
print(Name)
print("Your daily calories burnt from walking is", "{:.2f}". format(Daily_calories_burned))

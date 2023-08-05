#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
bill = float(input("what was the today bill? $"))
tip_percent=int(input("what percentage tip would you like to give?10, 12, or 15 : "))
tip_amount = (tip_percent/100)*bill
total_bill = float(bill + tip_amount)
split= int(input("how many people to split the bill? "))
per_person = round(total_bill/split,2)
print(f"Each person shuld pay: ${per_person}")

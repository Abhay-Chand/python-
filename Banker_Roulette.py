# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma\. \n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = len(names)
random_name = random.randint(0,x - 1)
person_who_pay_the_bill = names[random_name]
print( person_who_pay_the_bill + "is going to buy the meal today!")
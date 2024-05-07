#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#este programa calcula a gorjeta dada em um restaurante de acordo com a porcentagem digitada, e divide pelo numero de pessoas que pagará aconta

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
total_percentage = input("What percentage tipp would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

total_float_bill = float(total_bill)
total_int_percentage = int(total_percentage)
people_int = int(people)

percentage = total_float_bill * total_int_percentage / 100
total = (total_float_bill + percentage) / people_int
total_final = round(total,2)
total_final = "{:.2f}".format(total)

print (f"Each person should pay: round {total_final}")
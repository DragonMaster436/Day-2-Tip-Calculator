#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcom to the tip calculator! ")
bill = input("What was the total bill? ").replace('$', '')
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_as_int = float(bill)
tip_as_int = float(tip)
people_as_int = float(people)
bill_with_tip = tip_as_int / 100 * bill_as_int + bill_as_int

final = bill_with_tip / people_as_int
final_with_round = "{:.2f}".format(final)

print(final_with_round)


# note to self, this was hard lol 😭

# Program that calculates the fewest coins necessary to return change from
# an amount of dollars input as a float by a user
#
# Wouter Vrielink
# 09-02-2020

# get the amount of change due in dollars
dollars = float(input("How much change is owed?"))

# when the user uses values under 0, make sure to ask again
while dollars < 0:
    dollars = float(input("How much change is owed?"))

# convert to whole cents
cents = round(dollars * 100)

nr_coins = 0

# we have 4 types of coins (25, 10, 5, and 1 cents) which we will retrieve
# amounts for greedily one by one
while cents >= 25:
    cents -= 25
    nr_coins += 1

while cents >= 10:
    cents -= 10
    nr_coins += 1

while cents >= 5:
    cents -= 5
    nr_coins += 1

while cents >= 1:
    cents -= 1
    nr_coins += 1

print(nr_coins)

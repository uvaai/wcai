# Program that calculates the fewest coins necessary to return change from
# an amount of dollars input as a float by a user
#
# Wouter Vrielink
# 09-02-2020

def get_user_cents():
    # get the amount of change due in dollars
    dollars = float(input("How much change is owed?"))

    # when the user uses values under 0, make sure to ask again
    while dollars < 0:
        dollars = float(input("How much change is owed?"))

    # convert to whole cents and return
    return round(dollars * 100)


def greedy_change_calculator(cents, cointypes):
    nr_coins = 0

    # we have 4 types of coins (25, 10, 5, and 1 cents) which we will retrieve
    # amounts for greedily one by one
    for coin_type in cointypes:
        nr_coins += cents // coin_type
        cents %= coin_type

    return nr_coins


cointypes = [20, 10, 5, 1]

cents = get_user_cents()
nr_coins = greedy_change_calculator(cents, cointypes)
print(nr_coins)

# *****************************************************************************
# Author:           Mike Winebarger
# Program Name:     Lab 3
# Date:             October 24, 2021
# Description:      This program takes in Trimet pass type and tickets
#                   purchased and returns amount spent and tickets remaining to
#                   receive free rides for the rest of the month
# Input:            string passType, int ticketsPurchase
# Output:           float amountRemaining, float amountSpent vs freeLimit
# Sources:          Lab 3 Documentation, CS-161A project divided into modules
#                   and converted into Python. This was to attempt doing the
#                   same project in separate languages.
# ******************************************************************************


def main():
    intro_message()

    passType, fare, freeLimit = get_pass()
    numTickets = get_tickets()
    amountSpent, amountRemaining = amounts(fare, freeLimit, numTickets)

    output(amountSpent, amountRemaining)


def intro_message():
    print("Welcome to Trimet Hop Fastpass!\n")
    print("With Fastpass, adults ride free after purchasing $100 in tickets")
    print("in one month, while Honored and Youth fares ride free after $28!\n")
    print("Adult fare (ages 18-64) is $2.50 and Honored/Youth fare is $1.25.\n")


def get_pass():
    passType = str(input("Enter pass type (A: Adult, H: Honored, Y: Youth): "))
    passType = passType.lower()

    if passType != 'a' and passType != 'h' and passType != 'y':
        print("Invalid pass type!")
        exit(1)
    else:
        if passType != 'a':
            freeLimit = 28.00
            fare = 1.25
        else:
            freeLimit = 100.00
            fare = 2.50
        return passType, fare, freeLimit


def get_tickets():
    numTickets = int(input("Enter number of tickets purchased this month: "))
    return numTickets


def amounts(fare, freeLimit, numTickets):
    amountSpent = fare * numTickets
    amountRemaining = freeLimit - amountSpent
    return amountSpent, amountRemaining


def output(amountSpent, amountRemaining):
    print("\nYou have spent $", "%.2f" % amountSpent, " this month.")
    check_free(amountRemaining)


def check_free(amountRemaining):
    if amountRemaining > 0:
        print("Spend $", "%.2f" % amountRemaining, "more to earn free rides!")
    else:
        print("You have earned free rides for the rest of the month!")


main()

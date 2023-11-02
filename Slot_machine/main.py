import random

# for the simplicity we will use a 3*3 Slot machine
MAX_LINES = 3  # global constants to keep the function smooth
MAX_BET = 100
MIN_BET = 1

ROWS = 3  # number of rows
COLS = 3  # number of columns

symbol_count = {  # we define the reels using a dictionnary
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2

}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = [0]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


# to generate the outcome of the slot machine using the symbols, rows, columns
def get_slot_machine_spin(rows, cols, symbols):

    all_symbols = []
    # symbols.items will give us the key and the value while itterating.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # _ it's  (convention in python)) an annonymous var or (value is disregarded) in the sense where we want to loop over something but we do not care about the count or the itteration value so we will not have an unused value anymore
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):  # generate a col for every single column we have if we have 3 columns we need to execute the code down here 3 times and then we will generate random values for each row\ # we can also use here the _ we do not need col
        column = []
        # a copy of the list (if we did this: current_symbols = all_symbols[] it will be referencing any chnage in each list will be copied and carried into the next we do not want that), # Making a copy of the list to avoid referencing and hence modifying the original list.
        current_symbols = all_symbols[:]
        for _ in range(rows):  # we can also use here the _ we do not need row
            value = random.choice(current_symbols)  # pick a symbole randomly
            # delete the value after each itteration (deleting the old one) so we do not pick it again
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        # enumerte will give the index and as well the item
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # max index we have to access the columns list
                # a pipe operator to have some separation between the items
                # we added end="" to prevent the new line after the print statment
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()  # it will print an new line character it is used to create  aline break after printing each row of columns


def deposit():  # to collect and store user data
    while True:  # to get a valid amount from the users
        # a prompt to ask the user how much they want to deposit in dollars
        amount = input("How much would you like to deposit? $ ")
        if amount.isdigit():  # .isdigit is a string method that will check if the number is a whole number and not a negative number this will return a string
            amount = int(amount)  # convert the string to an integer amount
            if amount > 0:
                break  # if the amount the user entered is bigger then 0 then it will break out of the while loop
            else:
                # if the amount the user entered is smaller then 0 it will print the statmen
                print("Amount must be greater then 0. ")
        else:
            # if the amount typed by the user is not a number it will print this statment
            print(" Please enter a numerical value. ")
    # if all the conditions are met, it will return the number (amount)
    return amount


def get_number_of_lines():
    while True:

        # we converted the MAX_LINES to str and nut put a number so the printed experssion look good
        # ask the user to put a number of lines from 1-to MAX_lines here it will show 1-3 as input function always returns a string we needed to convert the MAX_LINES constant to  str
        lines = input(
            "Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # to see if the value is between  1 and 3
                break
            else:

                print("Enter a valid number of lines. ")
        else:

            print(" Please enter a number. ")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # when you use string formatting anything betwen {} is automatically converted to str by python
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number. ")
    return amount


def spin(balance):

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:  # we need to check if the total bet on each line doesn't exceed the total amount
            print(
                f"You do not have enough money to bet that amount,your current balance is :${balance} ")
        else:
            break
    print(
        f"You are betting ${bet} on {lines} Lines. Total bet is equal to: ${total_bet}")
    print(
        f"Your balance is: {balance}$ and the number of lines is: {lines} lines. ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    # *winning_lines the splat or unpack operator it will pass everything that is inside the winning_lines
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():  # we defined a new function called main so when we call main it will run all the code that is inside the function deposit
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()

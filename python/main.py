import random

MAX_BET = 100
MIN_BET =1
ROW = 3
COL = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "c" : 6,
    "d" : 8
}
def get_slot_machine_spin (row, col, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)


def deposit():
    while True:
        amount = int(input("Enter the amount $ :"))
        if (amount>0):
            # print(amount)
            break
        else:
            print("amount should be greater than 0")
    return amount 


def get_lines():
    while True:
        lines = int(input("Enter the no of lines 1-3 :"))
        if (1 <= lines <= 3):
            break
        else:
            print("Lines should be between 1-3")
    return lines

def get_bet():
    while True:
        amount = int(input("What would you like to bet on each line $ :"))
        if (1 <= amount <=100):
            break
        else:
            print("amount should be between 1 and 100")
    return amount

def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if (total >= balance):
            print(F"you dont have sufficent balance for bet , your current balance is ${balance}")
        else: 
            break
    print(F"you are betting ${bet} on {lines} line . Total bet is = ${total}")
   

main()
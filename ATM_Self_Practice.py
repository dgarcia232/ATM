# Program: ATM SIMULATOR
# Author: David Garcia
def main():
    print("WELCOME TO DAVID'S ATM")
    print()
    balance = get_balance()
    print('='* 45)
    #amount_deposited = deposit()
    #amount_withdrawaled = withdraw()
    get_display(balance)

def get_balance():
    balance = float(input('Enter a starting balance:'))
    while balance < 0:
        print('INVALID BALLANCE')
        balance = float(input('Enter a positive starting balance:'))
    return balance

def get_deposit():
    deposit = float(input('Enter the amount you would like to deposit:'))
    return deposit
                    
def get_withdraw():
    withdraw = float(input('Enter the amount you would like to withdraw:'))
    return withdraw

def get_display(balance):
    print('''Selection Options:

1.) Check balance

2.) Make a Deposit

3.) Make a withdrawal

4.) Exit ATM ''')
    print()
    selection(balance)

def selection(balance):
    selection = int(input('Enter your selection:'))
    while selection > 4 or selection < 1:
        print('INVALID INPUT')
        selection = int(input('Enter your selection (1-4):'))
        
    if selection == 1:
        print('your balance is',balance)
        print('='* 45)        
        get_display(balance)
    elif selection == 2:
        amount_deposited = get_deposit()
        balance += amount_deposited
        print('='* 45)
        get_display(balance)
    elif selection == 3:
        amount_withdrawaled = get_withdraw()
        if amount_withdrawaled > balance or amount_withdrawaled < 0:
            print('CANNOT WITHDRAWL MORE THAN YOUR CURRRENT BALANCE')
            print('='* 45)      
            get_display(balance)
        balance -= amount_withdrawaled
        print('='* 45)
        get_display(balance)
    elif selection == 4:
        print('Goodbye, have a nice day')
    

#call main
main()

import os

                                    #----------------------WITHDRAW FUNCTION----------------------

def withdraw(acc_balnce,acc_num,PIN):
    #Input Acc Number And PIN to Validate Already entered Account Number and PIN
    account=int(input("Enter Account Number: "))
    pin=int(input("Enter PIN: "))

    #If Acc number and PIN are Valide Then Take Amount To deposit else Throw Error Print 
    if account==acc_num and PIN==pin:
        #Max Amount of Withdraw
        max_withdraw=10000

        amount=float(input("Enter amount you want to withdraw: "))
        #If Amount Greater Than Max Withdraw or Amount Entered Is more Than Balance of User Throw A print Error.
        #Else Withdraw Amount
        if amount>max_withdraw:
            print("Entered Amount is more than Max withdraw in Single Transaction\n")
            print("Max Withdraw is",max_withdraw)
        elif amount>acc_balnce:
            print("Entered Amount is more than User Account balance\n")
        else:
            acc_balnce-=amount
            print(amount,"is withdraw successfully\n")
    else:
        print("Invalid Account Number Or PIN\n")
    return acc_balnce

                                #----------------------DEPOSIT FUNCTION------------------------------

def deposit(acc_balnce,acc_num,PIN):
    #Input Acc Number And PIN to Validate Already entered Account Number and PIN
    account=int(input("Enter Account Number: "))
    pin=int(input("Enter PIN: "))

    #If Acc number and PIN are Valide Then Take Amount To deposit else Throw Error Print
    if account==acc_num and PIN==pin:
        amount=float(input("Please Enter The amount you want to deposit: "))
        acc_balnce+=amount
        print("Amount is deposited Successfully\n")
    else:
        #Invalid Entry Of Either Account Number Or PIN
        print("Invalid Account Number Or PIN\n")
    return acc_balnce

                            #-------------------------CHECK BALANCE--------------------------------

def check_balance(acc_num,PIN,acc_balnce):
    #Print Balance Of Account Along with its PIN and Account Number
    print("Account Number:",acc_num," PIN: ",PIN," has Account Balance of ",acc_balnce,"\n")

                            #--------------------------MAIN PROGRAM------------------------

Account_num = int(input("Enter Account Number: "))
pin = int(input("Enter PIN: "))
balance=0
option=0
print("--------------ATM MACHINE------------------\n")
while True:
    print("---------User What would you like To do-------")
    print("1.Withdraw Amount")
    print("2.Deposit Amount")
    print("3.Check Balance")
    print("4.Exit")
    option=int(input("Select from 1,2,3 or 4: "))
    if option==1:
        balance = withdraw(balance,Account_num,pin)
    elif option==2:
        balance = deposit(balance,Account_num,pin)
    elif option==3:
        check_balance(Account_num,pin,balance)
    elif option==4:
        break
    else:
        print("INVALID SELECTION TRY AGAIN\n")

print("Thank you Please Come Again Sometime :)")

os.system('pause')
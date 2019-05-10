import random

def banking():
    try:
        password = int(input("\nPlease Enter Your 4-Digit OTP:\n"))
        otp = 1234
        if password != otp:    print("SORRY TRY AGAIN")
        if password==otp:
            print("\nWhat would you like to do today??  Please type the below options.\n")
            choice = input("\nNew Account\tWithdraw\tDeposit\t\tBalance Inquiry\t\tDemand Draft\tCancel\n\n")
            
            if choice == "new account":
                name = input("\nPlease Enter Your Name:\n")
                age = input("\nPlease Enter Your Age:\n")
                address = input("\nPlease Enter Your Address:\n")
                contact = input("\nPlease Enter Your Contact:\n")
                gender = input("\nPlease Enter Your Gender:\n")
                print("\nACCOUNT HOLDER DETAILS\n")
                print(name),(age),(address),(contact),(gender)
                print("\n")
            
            if choice == "withdraw":
                withdraw = int(input("\nEnter the Amount you want to Withdraw:\n"))
                if (withdraw >=100) and (withdraw <=10000):
                    print("\nHere is your money: ",withdraw)
                else:
                    print("\nLimit Exceeded\n")
            
            if choice == "deposit":
                while True:
                    deposit_amount = int(input("\nEnter the Amount you want to Deposit:\n"))
                    if (deposit_amount%5)==0:
                        print("\nYour Money has been deposited successfully!\n")
                        break
                    else:
                        print("\nPlease enter the valid amount\n")
                        continue
            
            if choice == "balance inquiry":
                print("\nDeposit Amount\t\tOutstanding Balance\t\tMinimum Due Amount\n")
                balance_choice=input("\nPlease Enter the above mentioned choices:\n")
                
            if choice == "demand draft":
                print("\nPlease Enter The Demand Draft Details:\n")
                bank_name = input("\nPlease Enter the Name of the Bank\n")
                account_holder = input("\nPlease Enter the Name of Account Holder\n")
                branch_name = input("\nPlease Enter the Branch Name\n")
                total_amount = input("\nPlease Enter the Total Amount\n")

            if choice == "cancel":
                while True:
                    print (name)
                    print (age)
                    print (address)
                    print (contact)
                    print(gender)
                    print(withdraw)
                    print(deposit_amount)
                    print(bank_name)
                    print(account_holder)
                    print(branch_name)
                    print(total_amount)
                    break                
    except ValueError or TypeError:
        print("\nThank you for your visit!!\n")

banking()
import csv
import time


Password = 1947
Balance = 50000
transactions = []


def save_transactions(transactions):
    with open('Transaction History.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Transaction Details', 'DR', 'CR'])
        writer.writerows(transactions)
    


print("Welcome To ABC Bank \nPlease Insert Your Card")
time.sleep(2)
print("Please Wait We Are Reading Your Card's Chip")
time.sleep(1)
pin = int(input("Please Enter Your Pin : "))


if pin == Password:
    print("Please Wait We Are Verifying...\n")
    time.sleep(2)
    print("Hello,Mr.Koushik Paul. Welcome To Our Bank, How We Can Help You ?\n")
    while True:
        print("Please Choose Any Option Below !! \n 1. Banking \n 2. Transaction History\n 3. Windrawl \n 4. Check Balance \n 5. Exit\n")
        choice = int(input("Enter your option: "))
        
        if choice == 1:
            option = input("\nChoose Any Option Below !!\n 1. Send Money \n 2. Transaction History \n 3. Rest Pin \n 4. Add Fund\n 5. Back\n\nEnter Your Option : ")
            
            if option == "1":
                print("\nSending Money By Account Number :\n")
                accountno = int(input("Please Enter The Account No. : "))
                ifsc = int(input("Please Enter The IFSC Code : "))
                
                if accountno == 1234567890:   
                    DR = int(input("Please Enter The Amount: ₹"))
                    userinput = input("Do You Want To Add More Amount ? \n::")
                    
                    if userinput =="Yes":
                        addamount = int(input("Please Enter The Amount : ₹"))
                        k = DR+addamount
                        
                        if k <= Balance:
                            Balance -= k
                            transactions.append(('Money Is credited To A/c: 1234567890', k, Balance))
                            print("\nMoney Send To A/c: 1234567890 : ₹", k)
                            print("\n")
                        else:
                            print("\nInsufficient Balance!\n")
                    
                    elif userinput == "No":
                        if DR <= Balance:
                            Balance -= DR
                            transactions.append(('Money Is credited To A/c: 1234567890', DR, Balance))
                            print("\nMoney Send To A/c: 1234567890 : ₹", DR)
                            print("\n")
                        else:
                            print("\nInsufficient Balance!\n")
                else:
                    print("PLease Choose The Correct Option")                 
            
            elif option == "2":
                print("\nTransaction History:")
                print("\n")
                for transaction in transactions:
                    time.sleep(1)
                    print(transaction[0] + ':', transaction[1])
                
                print("\nYour Available Balance is : ₹",Balance)
                time.sleep(1)
                
            elif option == "3":
                passcode = int(input("Please Enter Your Current Pin : "))
                if passcode == Password:
                    passcode = Password
                    time.sleep(1)
                    print("Your Password Change Successfully")
            
            elif option == "4":
                CR = int(input("Enter The Deposit Amount: ₹"))
                Balance += CR
                transactions.append(('Cash Deposite', CR, Balance))
                print("Cash Deposit : ₹", CR)

        elif choice == 2:
            print("\nTransaction History:")
            for transaction in transactions:
                time.sleep(1)
                print(transaction[0] + ':', transaction[1])
            print("\nYour Available Balance is : ₹",Balance)
            print("\n")
            time.sleep(1)

        elif choice == 3:
            DR = int(input("Please Enter The Amount You Withdrawl : ₹"))
            userinput = input("Do You Want To Add More Amount ? \n::")
            
            if userinput =="Yes":
                addamount = int(input("Please Enter The Amount : ₹"))
                k = DR+addamount
                
                if k <= Balance:
                    Balance -= k
                    transactions.append(('Cash Withdrawl From Bank', k, Balance))
                    print("Cash Withdrawl From Bank : ₹", k)
                    print("\n")
                else:
                    print("\nInsufficient Balance!\n")
            
            elif userinput == "No":
                
                if DR <= Balance:
                    Balance -= DR
                    transactions.append(('Cash Withdrawl From Bank', DR, Balance))
                    print("Cash Withdrawl From Bank : ₹", DR)
                    print("\n")
                else:
                    print("\nInsufficient Balance!\n")
        
        elif choice == 4:
            pas = int(input("\nPlease Enter Your Pin : "))
            
            if pas == Password:
                print("\nYour Available Balance is : ₹",Balance)
                print("\n")
                
        elif choice == 5:
            save_transactions(transactions)
            print("Exiting...")
            break
       
        else:
 
            print("Invalid option! Please choose again.")

else:
    print("Invalid PIN!")
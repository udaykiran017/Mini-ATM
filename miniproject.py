def ATM():
    print("please insert card")
    a=int(input("Enter 1 if you've inserted: "))
    if a==1:
        print("welcome Mr.john")
        b=10000
        print("YOUR ACCOUNT BALANCE IS :",b)
        password =9440
        count=0
        while count<3:
            pin=int(input("Enter PIN:"))
            count+=1
            if pin== password:
                print('''SELECT THE OPTION
                FOR CASH WITHDRAWAL-ENTER 2
                FOR DEPOSIT-ENTER 3
                FOR CHANGING THE PIN -ENTER 4''')
                x=int(input("Enter your choice: "))
                if x==2:
                    c=int(input("ENTER AMOUNT: "))
                    if b>=c:
                        print("TRANSACTION IS IN PROCESS")
                        b=b-c
                        print("Remaining balance is",b)
                        print("Thank you")
                        print("please visit again ")
                        break
                    else:
                        print('''Insufficient balance.
                        Thank you''')
                elif x==3:
                    print("Insert your money")
                    f=int(input("Enter the amount you inserted: "))
                    b+=f
                    print("Thank you for depositing your money.")
                    print("Your account balance is",b)
                    break
                elif x==4:
                    print("PIN CHANGE")
                    count1=0
                    while count1<3:
                        pin2=int(input("enter your new pin of 4 digits: "))
                        count1+=1
                        if pin!=pin2:
                            pin3=int(input("please re enter your pin again: "))
                            if pin2==pin3:
                                print("your new pin is updated")
                                password=pin3
                                break
                            else:
                                print("Pin not matched.")
                                break
                        else:
                            print("please enter a different pin. Thanks for visiting.")
                            break


                else:
                    print("Invalid Input")



            else:
               print("WRONG PIN ENTER AGAIN")





    else:
        ATM()
ATM()



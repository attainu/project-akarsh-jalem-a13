import time
class Payment:
    @staticmethod
    def order_payment(order):#a list which is dictionary where all food items and price is stored.
        selected_items = []
        for item in order:
            selected_items.append(item)
        print(">> You have selected: \n")
        for key in selected_items:
            print(key)
        print()
        sum = 0
        for i in order: 
            sum = sum + int(order[i])
            CGST = sum * (2.5/100)
            SGST = sum * (2.5/100)
            updated_sum = sum + CGST + SGST
        
        print(">> Your total amount of all items is ₹ : ",sum)
        print("CGST is:                                 ",CGST)
        print("SGST is:                                 ",SGST,"\n"*2)
        print("Final amount to be paid after CGST and SGST is ₹ : ",updated_sum)
        print()
        print(">> Please give your Contact Details")
        First_name = input("* First Name :")
        Last_name = input("* Last Name :")
        Phone_number =input("* Phone Number:")
        Address = input("* Address :")
        print(">> Please select the payment method : ")
        print()
        n = input(" 1.COD \n 2.UPI \n 3.Debit/Credit card \n\n>> Choose your option :")
        print("*" * 28)
        print(">> Your Delivery Details Are :")
        print(f" First name : {First_name}")
        print(f" Last name : {Last_name}")
        print(f" Phone number : {Phone_number}")
        print(f" Delivary Address : {Address}")
        print("*" * 28)
        time.sleep(2)
        print()
        
        if n == '1':
            print(">> Request has been accepted and you choose for COD")
            print()
            
        elif n == '2':
            n = input(">> Please enter your UPI ID: ")
            print()
            m = input(">> Enter pin :")
            print("Your payment is in progress.....")
            print() 
            time.sleep(3)
            print("Payment has been accepted")
            print()
        elif n == '3':
            print(">> Please enter your Card Details: ")
            print()
            m = input(">> Enter Card Number :")
            z = input(">> Enter CVV :")
            time.sleep(3)
            y = input(">> Enter OTP :")
            print("Your payment is in progress.....")
            print() 
            time.sleep(3)
            print("Payment has been accepted!!!!")
            print()
        print()       
           

        print("Your Food is preparing......")
        print()

        time.sleep(5)

        print("*" * 15 +"   Your food is ready and out for  delivery. It will reach by you in 20 minutes :)   " + "*" * 15)
        print()

        print("*" * 43 +"   HAPPY ORDERING   "+ "*" * 43)
        print()
        


from single_order import *
from multiple_order import * 
from Tikka_hut import *
from Surmai import *
from Dwara import *
from update_menu import *



sngl = Single_Order_Selection()
mul = Multiple_Order_Selection()
upd = Update_Menu()
res_A = Tikka_hut()
res_B = Surmai()
res_C = Dwara()
res_A.food_item()
res_B.food_item()
res_C.food_item()

print()
print( "* " * 7 + "      WELCOME TO CRAVINGZZ!!!     "+ "* " * 7)
print("  " + "* " * 10 + "   HELLO BUDDY!!   " + "* " * 9) 
print()
print(" >> Choose your option :-")
print()
print(" 1 To Go inside Application ")
print(" 2 To QUIT ")
print()
option=input(">> Enter your choice : ")
print()
if option == '1':
    print(">> You are:-  \n\n 1.CUSTOMER \n 2.OWNER ")
    print()
    op = input(">> Enter your choice :")
    print()
    if op == '1':
            
        print(" 1 to ORDER LOWEST PRICED FOOD AND TO ORDER SINGLE ITEM \n 2 to  SELECT RESTURANT AND ORDER MULTIPLE ITEM ")
        print()
        op = input(">> Enter your Choice :")
        print()
        if op == '1':
            sngl.single_order(res_A, res_B, res_C)
            
        elif op == '2':
            mul.multiple_order(res_A, res_B, res_C)
                    
    elif op == '2':
        upd.add_item(res_A, res_B, res_C)
            

        
else :
    print("*" * 15 +"   You choose to quit :) have a nice day come back soon :D   " + "*" * 15 )
    quit()

   

     
  
    
                                                                             
from Tikka_hut import *
from Surmai import *
from Dwara import *


class Update_Menu(Tikka_hut,Surmai,Dwara):

    def add_item(self,res_A, res_B, res_C):

        print("!!! We have the following restaurants !!!")
        print()
        
        print("1.Tikka_hut"," \n2.Surmai"," \n3.Dwara")
        print()
        self.res_name = input("Please select your restaurant by using no.: ")
        print()
        
        if self.res_name == '1':
            for key in res_A.menu_T:
                print(key,':',res_A.menu_T[key])
            # print("Your menu are: ",res_A.menu_T)
            print("Press : \n 1 to ADD ITEM \n 2 to REMOVE ITEM \n 3 to EXIT ")
            print()
            self.op = input("Choice :")
            print()
            if self.op == '1':
                print("item present in menu:")
                for key in res_A.menu_T:
                    print(key,':',res_A.menu_T[key])
                # print("Item present in the menu : ", res_A.menu_T)
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_A.menu_T[self.item]=self.price
                print("Updated menu :")
                for key in res_A.menu_T:
                    print(key,':',res_A.menu_T[key])
                # print("Your updated menu are: ",res_A.menu_T)

            elif self.op == '2':
                for key in res_A.menu_T:
                    print(key,':',res_A.menu_T[key])
                self.item = input("Type the item you want to remove: ")
                print()
                del res_A.menu_T[self.item]
                print("Your updated menu are:")
                for key in res_A.menu_T:
                    print(key,':',res_A.menu_T[key])
                # print("Your updated menu are: ",res_A.menu_T)
            
            elif self.op == '3':
                return 
                    
                    

        elif self.res_name == '2':
            print(">> Your menu are: ")
            for key in res_B.menu_S:
                print(key,':',res_B.menu_S[key])
            print()
            print(">> Press : \n\n1 to ADD ITEM \n2 to REMOVE ITEM \n3 to EXIT \n")
            self.op = input(">> Choice :")
            print()
            if self.op == '1':
                print("Item present in the menu :")
                for key in res_B.menu_S:
                    print(key,':',res_B.menu_S[key])
                # print("Item present in the menu : ", res_B.menu_S)
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_B.menu_S[self.item]=self.price
                print("Your updated menu are:")
                for key in res_B.menu_S:
                    print(key,':',res_B.menu_S[key])
                # print("Your updated menu are: ",res_B.menu_S)
                
            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del res_B.menu_S[self.item]
                print("Your updated menu are: ")
                for key in res_B.menu_S:
                    print(key,':',res_B.menu_S[key])
                # print("Your updated menu are: ",res_B.menu_S)
            
            elif self.op == '3':
                return
                        
                    

        elif self.res_name == '3':
            for key in res_C.menu_D:
                print(key,':',res_C.menu_D[key])
            # print("Your menu are: ",res_C.menu_D)
            print("Press: \n1 to ADD ITEM \n2 to REMOVE ITEM \n3 to EXIT ")
            self.op = input("Choice :")
            print()
            if self.op == '1':
                print("Item present in the menu : ")
                for key in res_C.menu_D:
                    print(key,':',res_C.menu_D[key])
                #print("Item present in the menu : ", res_C.menu_D)
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                res_C.menu_D[self.item]=self.price
                print("Your updated menu are: ")
                for key in res_C.menu_D:
                    print(key,':',res_C.menu_D[key])
                # print("Your updated menu are: ",res_C.menu_D)

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del res_C.menu_D[self.item]
                print("Your updated menu are: ")
                for key in res_C.menu_D:
                    print(key,':',res_C.menu_D[key])
                #print("Your updated menu are: ",res_C.menu_D)
            
            elif self.op == '3':
                return
        
       
        

          
#Online Store [FYI - all the options are working good...]

print("Welcome to the Store")
new_items = ["NC","NL"]
refurbished_items = ["RC","RL"]
pheripherals = ["MONITOR",
                "CPU",
                "KEYBOARD",
                "MOUSE",
                "MOUSEPAD",
                "CABLES"
                ]
total_cost = []

items = []

user_input = "-"

while user_input != "0":
    #if user_input in "M":
    if user_input == "M":
        print("Menu")
        print("1 - for new items")
        print("2 - for refurbished items")
        print("3 - for pheripherals")
        
        user_input1 = input("userinput1: ").upper()
        if user_input1 == "EXIT":
            print("you bought these items: ",items)
            print("Recipt for bill payment of RS: {}/-".format(sum(total_cost)))
            print("Thanks for visiting the store..."," ","Visit Again")
            break
        if user_input1 in "123":
            if user_input1 == "1":
                print("Available items in the New items: ",new_items)
                ne = input("Enter what you want from the above list of items? ").upper()
                if ne in new_items:
                    print("Yes it is Available")
                    if ne == "NC":
                        cost = 25000
                        print("cost of the new computer is: ", cost)
                        ip = input("are you willing to buy this: ").upper()
                        if ip == "YES":
                            total_cost.append(cost)
                            items.append("New Computer")
                        print("you total bill amount is :",sum(total_cost))
                            

                    if ne == "NL":
                        cost = 30000
                        print("cost of the new laptop is: ",cost)
                        ip = input("are you willing to buy this: ").upper()
                        if ip == "YES":
                            total_cost.append(cost)
                            items.append("New Laptop")
                                
                        print("you total bill amount is :",sum(total_cost))   
                else:
                    print("Please Enter Correct Input")
                    
            if user_input1 == "2":
                print("items Available in the Refurbished: ",refurbished_items)
                ne= input("Please enter the devie you want from the above list: ").upper()
                if ne == "RC":
                    cost = 20000
                    print("cost of the R computer is: ", cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Refurbished Computer")
                    print("you total bill amount is :",sum(total_cost))
                            

                if ne == "RL":
                    cost = 25000
                    print("cost of the R laptop is: ",cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Refurbished Laptop")
                                
                    print("you total bill amount is :",sum(total_cost))
                print("Please Enter correct input")
            if user_input1 == "3":
                print("Available items in the Pheripherials: ",pheripherals)
                ne= input("Please enter the devie you want from the above list: ").upper()
                if ne == "MONITOR":
                    cost = 12500
                    print("cost of the Monitor is: ", cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Monitor")
                    print("you total bill amount is :",sum(total_cost))
                            

                if ne == "CPU":
                    cost = 18000
                    print("cost of the CPU is: ",cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("CPU")
                                
                    print("you total bill amount is :",sum(total_cost))

                
                if ne == "KEYBOARD":
                    cost = 1000
                    print("cost of the Keyboard is: ", cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Keyboard")
                    print("you total bill amount is :",sum(total_cost))
                            

                if ne == "MOUSE":
                    cost = 475
                    print("cost of the Mouse is: ",cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Mouse")
                                
                    print("you total bill amount is :",sum(total_cost))
                
                if ne == "MOUSEPAD":
                    cost = 250
                    print("cost of the Mousepad is: ", cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Mousepad")
                    print("you total bill amount is :",sum(total_cost))
                            

                if ne == "CABLES":
                    cost = 120
                    print("cost of the cable is: ",cost)
                    ip = input("are you willing to buy this: ").upper()
                    if ip == "YES":
                        total_cost.append(cost)
                        items.append("Cable")
                                
                    print("you total bill amount is :",sum(total_cost))
                        
        
                
        if user_input != "123":
            continue
                    
    if user_input == "0":
        print("Exit")
    
    else:
        print("PLease Choose the below Options")
        print("M - Menu")
        print("Press any key to EXIT")
    user_input = input("userinput: ").upper()
    if user_input != "M":
        break


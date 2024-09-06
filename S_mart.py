import datetime
import time 

info = """
1 : About S_mart.
2 : list of items avaiable at the store.
3 : about the deal of the day.
4 : to buy an item.
0 : To exit."""

# Available_items = {'sugar': 40 ,'salt': 30,'milk': 70,'rice' : 48,'milkbread' : 60, 'paste': 50}

supermarket_items = {
    "Fruits & Vegetables": {
        "Apple": 150,   # Price per kg
        "Banana": 50,   # Price per dozen
        "Tomato": 30,   # Price per kg
        "Potato": 40,   # Price per kg
        "Onion": 60     # Price per kg
    },
    "Dairy Products": {
        "Milk": 50,     # Price per liter
        "Cheese": 250,  # Price per 500g
        "Butter": 200,  # Price per 500g
        "Yogurt": 40    # Price per 500g
    },
    "Bakery": {
        "Bread": 30,    # Price per loaf
        "Cake": 300,    # Price per kg
        "Cookies": 100, # Price per 500g
        "Croissant": 50 # Price per piece
    },
    "Beverages": {
        "Tea": 200,     # Price per kg
        "Coffee": 500,  # Price per kg
        "Juice": 80,    # Price per liter
        "Soda": 40      # Price per liter
    },
    "Snacks": {
        "Chips": 20,    # Price per pack
        "Biscuits": 40, # Price per pack
        "Namkeen": 150, # Price per kg
        "Chocolate": 100 # Price per 100g
    },
    "Household Essentials": {
        "Detergent": 300, # Price per kg
        "Soap": 25,       # Price per bar
        "Shampoo": 150,   # Price per 200ml
        "Toothpaste": 70  # Price per 100g
    }
}

About = """
Welcome to S-Mart, your one-stop destination for all your shopping needs!

About Us:
Hi, my name is Satya Venkat Kurella, and I am excited to introduce S-Mart, your neighborhood supermarket.\nWe are open from 9:00 AM to 9:00 PM at all our branches across India. Our aim is to provide a seamless shopping experience with a wide range of products to cater to your daily needs.

Features:

*Wide Range of Products: From fresh produce to household essentials, find everything you need in one place.
*Convenient Shopping Hours: Shop at your convenience from 9:00 AM to 9:00 PM every day.
*Multiple Locations: Visit any of our branches across India for a consistent and reliable shopping experience.
*Customer Support: Have any queries? Our helpdesk is always ready to assist you. Reach out to us for any support you need\n"Smartsupport@gmail.com".
Thank you for choosing S-Mart. We look forward to serving you!
"""
# if inp1 == 1:5
#     print(About_sm)
# else:
#     print("please select in between 0,1,2,3")

cart_items = []
cart_price = [] 

while True:
    print(info)
    inp1 = int(input("Enter input: "))
    if inp1 == 1:
        print(About)

    if inp1 == 2:
        print(f"there are the available items under the below Catergories at the Store...")
        items_category = {1: 'Fruits & Vegetables', 2 : 'Dairy Products',3 : 'Bakery',4 : 'Beverages',5 : 'Snacks',6 : 'Household Essentials'}

        for i,j in supermarket_items.items():
            print(f"{i} {j}")

        # for i,j in items_category.items():
        #     print(f"{i} : {j}")
        
        # select_category = True    

        # if select_category == True:
        #     inp2 = int(input("select Category : "))
        #     print(supermarket_items[items_category[inp2]])
        # if select_category == False:
        #     print(f"Back to Main menu") 
            


    if inp1 == 3:
        print(f"No deal present for the day")

    if inp1 == 4: 
        
        print(f"there are the available Categories at the Store...")
        items_category = {1: 'Fruits & Vegetables', 2 : 'Dairy Products',3 : 'Bakery',4 : 'Beverages',5 : 'Snacks',6 : 'Household Essentials'}

        for i,j in items_category.items():
            print(f"{i} : {j}")

        select_category = True    

        if select_category == True:
            inp2 = int(input("select Category : "))
            print(supermarket_items[items_category[inp2]])
            inp3 = input("Select from the above item: ")
            selected_item_price = (supermarket_items[items_category[inp2]][inp3])
            cart_price.append(selected_item_price)
            cart_items.append(inp3)
            print(f"items added in the cart {cart_items}")
            print(f"price of the items in the cart :{cart_price}")  
        

            any_other = input("do you want anything from this category : ").upper()
            while any_other == "YES":
                select_category = True
                print(supermarket_items[items_category[inp2]])
                inp3 = input("select from the above items: ")
                selected_item_price = supermarket_items[items_category[inp2]][inp3]
                cart_price.append(selected_item_price)
                cart_items.append(inp3)
                print(f"items added in the cart {cart_items}")
                print(f"price of the items in the cart :{cart_price}")  
                inp3 == False
                any_other = False
           
        print(f"items added {cart_items}")
        print(f"price of the item {cart_price}")

        print(dict(zip(cart_items,cart_price)))

        
    # if inp1 == 5:
    #     print(f"{cart_items}")
    #     print(f"total amount : {sum(cart_price)}") 
    #     print(f"Thanks for shopping in Smart")
    if inp1 == 0: 
        print(f"Total items : {cart_items}")
        print(f"total amount : {sum(cart_price)}") 
        break
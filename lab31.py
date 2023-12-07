#Written by Pratik Shrestha(23026137)
#this is the program for lab-3
#Creating a menu for the AMANDO SHOPPING SITE
emp_dictionary={}    #defining an empty dictionary acc to qust
print ("""
WELCOME TO THE AMANDO SHOPPING SITE
    1.Add a Product to the cart
    2.Search for a product
    3.Delete a product from the cart
    4.Display the contents of the cart
    5.Purchanse items
    6.Quit
    """)
user_input=int(input("Enter what you want to choose:"))

#when the user input is not equal to 6, it will ask user again and again due to while loop

#defining this dic_function to check if the product detail is more than 5 then it will show the cart is empty
def dic_function(product_name, product_price, brand_name):
    if len(emp_dictionary) > 5:
        print("Sorry,The cart is full.")    
    else:
        emp_dictionary[product_name] = {"product-price": product_prices, "brand-name": brand_name}
        print()

#defining the function for the purchase(QN-5) as 
def to_purchase():
    total_price = sum(product_details["product-price"] for product_details in emp_dictionary.values())
    while True:
      answer = input("To complete Purchase; Choose(Y/N) ")
      if answer.lower() == "y":
          print("Thank you for your business.")
          print("Your Total is:",total_price)
          emp_dictionary.clear()
          break
      elif answer.lower() == "n":
          print("Please continue shopping.")
          break
      else:
          print("Please answer either Y or N.") 

while(user_input!=6):
    if(user_input==1):
            product_name=input("Enter the Product Name:")
            product_prices=float(input("Enter the Product Price:"))
            brand_name=input("Which brand do you prefer:")
            print("Item added to the cart")
            dic_function(product_name, product_prices, brand_name)
    elif(user_input==2):
            search_product=input("Enter the Product Name:")
            if(search_product in emp_dictionary):
                print(search_product,"=",emp_dictionary[search_product])
            else:
                print("This item is not in cart!")

    elif(user_input==3):
            del_detail=input("Enter the Product you want to delete:")
            if(del_detail in emp_dictionary):
                del emp_dictionary[del_detail]
                print(del_detail,"is deleted from the cart.")
                print("Only",emp_dictionary,"is in the cart")
            else:
                print("This item is not in cart!")

    elif(user_input==4):
            if(emp_dictionary!=0):
                print("You have",emp_dictionary,"item in the cart.")
            else:
                print("Sorry, the cart is empty")
    
    elif(user_input==5):
        to_purchase()

    elif(user_input==6):
        print()
    else:
        print("Invalid Input\n")

    print ("""
WELCOME TO THE AMANDO SHOPPING SITE
    1.Add a Product to the cart
    2.Search for a product
    3.Delete a product from the cart
    4.Display the contents of the cart
    5.Purchase items
    6.Quit
    """)
    user_input=int(input("Enter what you want to choose:"))




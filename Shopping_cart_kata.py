import json

#dictionary to store item prices and special bundle price
item_price = {
    "A": {"price": 50, "special_price": {"quantity": 3, "price": 140}},
    "B": {"price": 35, "special_price": {"quantity": 2, "price": 60}},
    "C": {"price": 25},
    "D": {"price": 12}
}


def calculate_subtotal(cart):

    subtotal = 0  #store the total as it increments, starting at 0

    for item in cart: #loop to go through each item in dictionary
        code = item["code"]
        quantity = item["quantity"] #extracts product code and quantity of current item in cart
        
        if code not in item_price:
            print(f"Error: Product with code '{code}' not found in pricing data")
            continue #skips to next iteration if  there is error
       
        if quantity < 0: #if quantity is below 0, outputs error message
            print(f"Error: Code '{code}' quantity '{quantity}' is out of range")
            continue
        

        price = item_price[code]["price"]  #retrieve price and special price of product 'code' from dictionary
        special_price = item_price[code].get("special_price") #using .get() to safely access special price without raising error 
                                                                #if it doesnt exist.
        
        if special_price:
                    #calculates number of times the special price applies and the remaining regular units
                    special_discount_units = quantity // special_price["quantity"]
                    regular_units = quantity % special_price["quantity"]
                    
                    #calculates subtotal with special discount applied for every group of special_price["quantity"]
                    subtotal += special_discount_units * special_price["price"] + regular_units * price
        else:
                    subtotal += quantity * price
    
    return subtotal



if __name__ == "__main__":

    with open("data-set-1.json", "r") as file: #opens a data-set-1.json file in read mode only
        shopping_content = file.read()  #reading file

    cart = json.loads(shopping_content) # converts json string into dictionary using json.loads() function
    subtotal = calculate_subtotal(cart) #calls calculate_subtotal function with 'cart' data as argument.
    print("Subtotal:", subtotal)

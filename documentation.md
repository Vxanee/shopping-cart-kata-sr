# **Shopping Cart Kata**

## **Description**
This is a simple python script for a checkout system for a shopping cart. It consumes a JSON data source containing the product codes and quantities for items in the cart and calculates the subtotal based on predefined item prices and special bundle prices.



## **Usage**
To use the script, follow these steps:

1. Repare your input data in a JSON format.
2. Ensure that the input data contains the product codes and quantities.
3. Run the script, providing the input JSON file as an argument.


Example command:

```

 with open("data.json", "r") as file:
    shopping_data = file.read()  # Read the file contents

```
## **Functionality**
The `calculate_subtotal` function in this script performs the following tasks:

* What it does: Calculates the subtotal of the items in the cart.
* Parameters:
    * `cart (dict)`: A dictionary representing the products and their quantities. Each dictionary should contain the following keys:
        * "code": The product code (string).
        * "quantity": The quantity of the product (integer).

* Returns:
    * `subtotal (float)`: The subtotal of the items in the cart.


## **Tests**
To run unit tests, execute `unittests.py` in the project directory.
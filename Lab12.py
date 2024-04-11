# Lab 12
# Author:

# Lab 12 will show basic understanding of Object Oriented Programming in Python.


# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)


# 2. Create a method called __str__ that returns a string with the following format:
# Product: <name>, Price: <price>, ID: <product_id>
# Hint: use f-strings to format the string.


# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.
# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.


# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.


# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.


# 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
# Hint: you will need to loop through the cart and add up the prices.


# 7. Create a method called display_products that prints out all the products in the cart list.(use the __str__ method from the Product class)


# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
# Make a nice table table using the tabulate library.


# 9. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.

# 10. Create a method called add_product that takes in a Product object and adds it to the products list.


# 11. Create a method called add_customer that takes in a Customer object and adds it to the customers list.

# 12. Create a method called display_products that prints out all the products in the products list.

# 13. Create a method called display_customers that prints out all the customers in the customers list.

# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 14. Create a store object called store.

# 15. Create a product object called product1 with the following attributes:
# name: "iPhone 12"
# price: 799.99
# product_id: 1

# 16. Create a product object called product2 with the following attributes:
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2


# 17. Create a product object called product3 with the following attributes:
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3

# 18. Create a customer object called customer1 with the following attributes:
# name: "John"
# customer_id: 1

# 19. Create a customer object called customer2 with the following attributes:
# name: "Jane"
# customer_id: 2


# 20. Add product1 to the store using the add_product method.

# 21. Add product2 to the store using the add_product method.

# 22. Add product3 to the store using the add_product method.

# 23. Add customer1 to the store using the add_customer method.

# 24. Add customer2 to the store using the add_customer method.

# 25. Add product1 to customer1's cart using the add_to_cart method.

# 26. Add product2 to customer1's cart using the add_to_cart method.

# 27. Add product3 to customer2's cart using the add_to_cart method.

# 28. Display current products in customer1's cart using the display_products method.

# 29. Display current products in customer2's cart using the display_products method.

# 30. Checkout customer1's cart using the checkout method.

# 31. Checkout customer2's cart using the checkout method.

# 32. Display current products in customer1's cart using the display_products method. (should be empty)

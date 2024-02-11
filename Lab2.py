# Lab2
# Author: Vadym Didukh

"""_summary_
This lab is designed to get you familiar with Python Data Types, Variables, and Arithmetic Operators.
"""

# 1. Create a variable called "name" and assign it the value of your name. Print the variable.
name = "Vadym Didukh"
print(name) 
# 2. Create a variable called "age" and assign it the value of your age. Print the variable.
age = 35 
print(age)
# 3. Create a variable called "favorite_color" and assign it the value of your favorite color. Print the variable.
favorite_color = "Blue" 
print(favorite_color)
# 4. Create a variable called "favorite_movie" and assign it the value of your favorite movie. Print the variable.
favorite_movie = "The Equalizer"
print(favorite_movie)
# 5. Use string concatenation to print the following sentence: "Hello, my name is <name>. I am <age> years old. My favorite color is <favorite_color> and my favorite movie is <favorite_movie>."
# Note: punctuation and capitalization matters. Make sure your sentence matches the one above exactly.
print("Hello, my name is " + name +". I am " + str(age) +" years old. My favorite color is " + favorite_color + " and my favorite movie is " + favorite_movie + ".")
# 6. Create a variable called "my_age_in_dog_years" and assign it the value of your age multiplied by 7.
my_age_in_dog_years = age * 7
# 7. Create a variable called "days_in_a_year" and assign it the value of 365.
days_in_a_year = 365
# 8. Create a variable called "days_alive" and assign it the value of your age multiplied by the number of days in a year.
days_alive = age * days_in_a_year
# 9. Create a variable called "days_alive_in_dog_years" and assign it the value of your age in dog years multiplied by the number of days in a year.
days_alive_in_dog_years = my_age_in_dog_years * days_in_a_year
# 10. Create a chart that shows the following information:
# - Your name
# - Your age
# - Your favorite color
# - Your favorite movie
# - Your age in dog years
# - Number of days in a year
# - Number of days you have been alive
# - Number of days you have been alive in dog years
print("==================================")
print("| Name: " + name + "             |")
print("| Age: " + str(age) + "                        |")
print("| Favorite Color: " + favorite_color + "           |")
print("| Favorite Movie: " + favorite_movie + "  |")
print("| Age in Dog Years: " + str(my_age_in_dog_years) + "          |") 
print("| Days in a Year: " + str(days_in_a_year)  + "            |")
print("| Days Alive: " + str(days_alive) +"              |")
print("| Days Alive in Dog Years: " + str(days_alive_in_dog_years) + " |")
print("==================================")
"""
Make it look pretty as well as informative. Use the following format:
==================================
| Name: John Doe                 |
| Age: 25                        |
| Favorite Color: Blue           |
| Favorite Movie: The Matrix     |
| Age in Dog Years: 175          |
| Days in a Year: 365            |
| Days Alive: 9125               |
| Days Alive in Dog Years: 63875 |
==================================
Hints:
- Use the string concatenation operator (+) to combine strings and variables
- print has an optional parameter called "end" that can be used to change the default newline character (\n) to something else or maybe even add a tab (\t) to the end of the line (or multiple tabs)
- You will need to use conversion functions to convert your numbers to strings
"""

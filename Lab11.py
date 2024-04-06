# Lab 11
# Author: Vadym Didukh

# Lab 11 will show demonstrate how Dictionary's work in Python.

# 1. Create a dictionary called my_dict with the following key value pairs:
# Key: "name", Value: "John"
# Key: "age", Value: 30
# Key: "city", Value: "Trenton"
# Key: "state", Value: "New Jersey"
my_dict = {"name": "Jhon", "age": 30, "city": "Trenton", "state": "New Jersey"}

# 2. Print out the dictionary.
print(my_dict)

# 3. Print out the value for the key "name".
print(my_dict["name"])
# 4. Lookup the key associated with the value "New Jersey" and print it out.
# Hint 1: You will need to loop through the dictionary.
# Hint 2: remember you can use the .items() method to get the key and value.
print(my_dict.items())

for item in my_dict.items():
    if item[1] == "New Jersey":
        print(item[0])
# 5. Add a new key value pair to the dictionary.
# Key: "country", Value: "USA"
my_dict["country"] = "USA"

# 6. Print out the dictionary.
print(my_dict)
# 7. Remove the key value pair with the key "city".
del my_dict["city"]
# 8. Print out the dictionary.
print(my_dict)
# 9. Create a dictionary called cities with an key as the City name and values as a dictionary that contains the state, population, and country.
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA
cities = {"Trenton": {"state": "New Jersey", "Population": 84913, "Country": "USA"},
          "New York City": {"state": "New York", "Population": 8336817, "Country": "USA"},
          "Los Angeles": {"state": "California", "Population": 3979576, "Country": "USA"},
          "Chicago": {"state": "Illinois", "Population": 2693976, "Country": "USA"},
          "Phoenix": {"state": "Arizona", "Population": 1680992, "Country": "USA"},
          "Philadelphia": {"state": "Pennsylvania", "Population": 1584138, "Country": "USA"},
          "San Antonio": {"state": "Texas", "Population": 1547253, "Country": "USA"},
          "San Diego": {"state": "California", "Population": 1423851, "Country": "USA"},          
}

print("======================================================")


# 10. Print a table of the data using the pandas library.
# pip install pandas
import pandas as pd
df = pd.DataFrame(cities)
print(df)

df = df.T
print(df)

print("=======================================================")

# 11. Use the tabulate library to print out the table.
# pip install tabulate
import tabulate
print(tabulate.tabulate(df, headers="keys", tablefmt="grid"))

# 12. Print out the population for the city of Chicago.
print(cities["Chicago"]["Population"])

# 13. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.
print("============================================")

data = [{"City": city, **info}for city, info in cities.items()]
# In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.
print(data)
# For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# The ** operator unpacks the info dictionary into the new dictionary

# Transform the data
headers = data[0].keys()
# Print the table using tabulate
print(tabulate.tabulate(data, headers="keys", tablefmt="fancy_grid"))

# 14. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.
count = 0
for city, info in cities.items():
    if info["Population"] > 1000000:
        count += 1
print(f"There are {count} cities with a population greater than 1 million.")        
# 15.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():

count_cities = 0
for city, info in cities.items():
    if info["Country"] == "USA":
        count_cities += 1
        
print(f"There are {count_cities} cities in the USA.")        
         



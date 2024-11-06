"""
Problem 1: Fruits and Statements
Create a function named list_fruits() that returns the following list of fruits: "Apple", "Banana", "Orange", "Mango".

Create a function named build_fruit_statement(fruit) which receives a string argument representing a fruit and returns a sentence that starts with the given fruit and ends with " is a delicious fruit."

Call list_fruits() and use build_fruit_statement() to print statements for each fruit.

"""

def list_fruits():
    return ["Apple", "Banana", "Orange", "Mango"]

def build_fruit_statement(fruit):
    return f"{fruit} is a delicious fruit."

fruits = list_fruits()
for fruit in fruits:
    print(build_fruit_statement(fruit))

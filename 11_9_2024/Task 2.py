"""
Problem 2: Countries and Capitals
Create a function named list_countries() that returns the following list of countries: "India", "USA", "Germany", "Australia".

Create a function named capital_of(country) which receives a string argument representing a country and returns the name of its capital. For example, "India" should return "New Delhi".

Call list_countries() and use capital_of() to print statements about each country and its capital, like "The capital of India is New Delhi."

"""

def list_countries():
    return ["India", "USA", "Germany", "Australia"]

def capital_of(country):
    capitals = {
        "India": "New Delhi",
        "USA": "Washington, D.C.",
        "Germany": "Berlin",
        "Australia": "Canberra"
    }
    return capitals.get(country, "Unknown")

countries = list_countries()
for country in countries:
    print(f"The capital of {country} is {capital_of(country)}.")

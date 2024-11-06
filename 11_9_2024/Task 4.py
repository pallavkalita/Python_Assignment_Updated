"""
Problem 4: Planets and Distances
Create a function named list_planets() that returns the following list of planets: "Mercury", "Venus", "Earth", "Mars".

Create a function named distance_from_sun(planet) which receives a string argument representing a planet and returns its average distance from the Sun in millions of kilometers. For example, "Earth" should return "149.6 million km."

Call list_planets() and use distance_from_sun() to print statements about each planet’s distance from the Sun, like "Earth is 149.6 million km away from the Sun."

"""

def list_planets():
    return ["Mercury", "Venus", "Earth", "Mars"]

def distance_from_sun(planet):
    distances = {
        "Mercury": "57.9 million km",
        "Venus": "108.2 million km",
        "Earth": "149.6 million km",
        "Mars": "227.9 million km"
    }
    return distances.get(planet, "Unknown distance")

planets = list_planets()
for planet in planets:
    print(f"{planet} is {distance_from_sun(planet)} away from the Sun.")

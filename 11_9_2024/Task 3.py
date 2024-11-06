"""
Problem 3: Animal Sounds
Create a function named list_animals() that returns the following list of animals: "Dog", "Cat", "Cow", "Lion".

Create a function named animal_sound(animal) which receives a string argument representing an animal and returns the sound it makes. For example, "Dog" should return "barks".

Call list_animals() and use animal_sound() to print statements about each animal and its sound, like "A Dog barks.
"""


def list_animals():
    return ["Dog", "Cat", "Cow", "Lion"]

def animal_sound(animal):
    sounds = {
        "Dog": "barks",
        "Cat": "meows",
        "Cow": "moos",
        "Lion": "roars"
    }
    return sounds.get(animal, "makes a sound")

animals = list_animals()
for animal in animals:
    print(f"A {animal} {animal_sound(animal)}.")

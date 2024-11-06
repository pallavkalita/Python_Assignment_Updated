
"""
Task: In this exercise, you will create a program by defining two functions and utilizing them together.

Create a function named list_languages() that returns the following list of programming languages: "Python", "Java", "C++", "JavaScript".

Create a function named build_statement(language) which receives a string argument representing a programming language and returns a sentence that starts with the given language and ends with " is a popular programming language."

Run and see how both functions work together by calling list_languages() and using build_statement() to print sentences for each language returned by list_languages().

"""

def list_languages():
    return ["Python", "Java", "C++", "JavaScript"]

def build_statement(language):
    return f"{language} is a popular programming language."

for lang in list_languages():
    print(build_statement(lang))



def list_languages():
    return ["Python", "Java", "C++", "JavaScript"]

def build_statement(language):
    return f"{language} is a popular programming language."

for lang in list_languages():
    print(build_statement(lang))

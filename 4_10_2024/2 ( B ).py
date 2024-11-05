
strings = []

def add_excitement(strings):
    

    strings_new = []
    
    for x in range(len(strings)):
        
        strings_new.append(strings[x] + "!")
        
    
    return strings_new
 
    
strings = [ "hi" , "hello" ]

print(f"Original String List : {strings}")


strings_new = add_excitement(strings)
print(f"Updated new List : {strings_new}")
print(f"Original String List : {strings}") #From this we know that the original list is not changed

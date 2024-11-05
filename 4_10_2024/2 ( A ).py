
strings = []

def add_excitement(strings):
    
    for x in range(len(strings)):
        strings[x] = strings[x] + "!"
        
    
    print(f"Updated String : {strings}")
 
    
strings = [ "hi" , "hello" ]

print(f"Original String List : {strings}")


add_excitement(strings)

print(strings) #From this we know that the original list is changed
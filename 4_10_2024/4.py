

def dig_root(n):
    
    while len(n) > 1:
    
        sum = 0
        
        
        for x in range(len(n)):
            
            sum = sum + int(n[x])
            
        n = str(sum)  
        
    return int(n)

n = input("Enter a number: ")

dig_rootnum = dig_root(n)

print("Digital Root:", dig_rootnum)

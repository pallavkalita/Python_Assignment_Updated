
def rectangle (m,n):
    
    for x in range(m):
        for y in range (n):
            print("*", end="")
        print()
            
            
m = int(input("Enter Rows : "))
n = int(input("Enter Columns : "))
print()
           
rectangle(m,n)
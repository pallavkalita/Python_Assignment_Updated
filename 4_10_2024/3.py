

def sum_digits(num):
    
    sum = 0
    for x in range(len(num)) :
       
        sum = sum + int(num[x])
        
    print(f"Sum of Digit : { sum } ")
     


num = input("Enter a number : ")
          
sum_digits(num)
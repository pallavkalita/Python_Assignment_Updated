# Understanding recursion using python


def recur(n):
    if n <= 0:
        return
    else:
        print(n)
        recur(n - 1)  
        
recur(5)

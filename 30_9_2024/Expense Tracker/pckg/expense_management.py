def add_expense(month, categ , descp, amount):
    list_expense = []
    month_expense = {}
    list_expense.append((categ, descp, amount))
    
    month_expense[month] = list_expense
    
    

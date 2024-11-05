from pckg.expense_management import add_expense
from pckg.monthly_report import total_expense

list_expense = []
expense_tuple = ()
month_expense = {}
sum = 0



month = input(" Enter Month : ")
n = int(input("Enter number of expenses : "))

for i in range(n):
   
    categ = input(" Enter Category : ")
    descp = input(" Enter Description : ")
    amount = int(input( " Enter Amount : "))
    add_expense(month , categ , descp, amount)
    sum = total_expense(amount) + sum

print(f"Total amount this month is : {sum}")

    

    
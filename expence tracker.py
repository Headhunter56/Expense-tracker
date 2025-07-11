expense=[]
total_amount=[]

def new_expense(a,b,c):
    new_expenses = {
            "amount": a,
            "category": b,
            "date": c
        }
    expense.append(new_expenses)

def view_all_expenses():
    for expenses in expense:
        print(f'expenses: {expenses}')

def total_spent():
    if not total_amount:
        print("empty")
    else:
        total=sum(total_amount)
        print(f"total:{total}")

def filter_by_category(catgrys):
    found=True
    for things in expense:
        if things["category"].lower()==catgrys.lower():
            print(f'amount:{things["amount"]}\ncategory:{things["category"]}\ndate:{things["date"]}')
    if not found:
        print("Maybe empty or invalid")

johny=True
while johny:
    print("1.Add new Expense")
    print("2.View all Expenses")
    print("3.View total spent")
    print("4.Filter by category")
    #print("5.save expenses to file")
    #print("6.load expenses from file")
    print("7.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        amount=int(input("Enter the amount to be added:"))
        print("category:\nFood,\nTransport,\nrent,\nRent,\nUtilities,\nEducation,\nshopping,\nHealth,\nEntertainment,\nwork,others")
        category=input("enter the category:")
        print("date_of_input")
        day=input("enter the day :")
        month=input("enter the month :")
        year=input("enter the year :")
        date_of_input=f'{day}-{month}-{year}'
        total_amount.append(amount)
        new_expense(amount,category,date_of_input)

    elif choice=="2":
        view_all_expenses()         #done

    elif choice=="3":
        total_spent()               #done

    elif choice=="4":
        filter_cat=input("enter the category you needed to check:")
        filter_by_category(filter_cat)          #done
    else:
        john=False
        print("By Bye Exiting")



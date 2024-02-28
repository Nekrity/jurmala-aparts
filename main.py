
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

apartments_price=apartments.copy()

# print(apartments)
def sort_price(apartments_price):
    return int(apartments_price[8])
while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        number=int(input("Enter apartment sequence number "))
        print(apartments[number-1])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        apartments_price.sort(key=sort_price, reverse = True)
        print(apartments_price[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        apartments_price.sort(key=sort_price)
        print(apartments_price[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        price=int(input("enter your price "))
        apartments_price.sort(key=sort_price)
        apartments_price_comparison=[x for x in apartments_price if int(x[8])<price]
        print(apartments_price_comparison[0:20])
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass
    elif choice == '5':
        price=int(input("enter your price "))
        apartments_price.sort(key=sort_price)
        apartments_price_comparison=[x for x in apartments_price if int(x[8])>price]
        print(apartments_price_comparison[0:20])
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass

    elif choice == '6':
        # 
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")



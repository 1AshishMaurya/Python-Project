list = []
Amount = 0
while(True):
    
    price = input("Enter The price of Item otherwise press q for quit :")
    if(price != "q"):
        list.append(price)
        Amount += int(price)
    else:
        print(f"Price List of items {list}\nYour Total Payable Amount = {Amount}")
        print("Thank You for comming Our Shop \nVisite Again")
        break



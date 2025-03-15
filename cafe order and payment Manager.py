# Manu
Manu = {
    "Pizza" : 100,
    "Burger" : 60,
    "Coffee" : 50,
    "Momos" : 40,
    "Tea" : 20,
    "Water" : 20
}
# food Manu on output window

print("Food Manu of our retaurent")
print("Pizza = 100\nBurger = 60\nCoffee = 50\nMomos = 40\nTea = 20")

# Order From Customer & Payment calculation
Amount = 0
Order = input("Order please which you want :")

if(Order not in Manu):
    print(f"Sorry..! {Order} is not in our Manu. Please select item from Manu")

else:
    Amount += Manu[Order]

    Water_Bottle = input("Do you Want Bottle Water Yes/No :")
    if(Water_Bottle == "Yes"):
        Amount += Manu["Water"]


    Other_Order = input("Do you want any other answer in Yes/No :")
    if(Other_Order == "Yes"):
        Order2 = input("Order Please :")
        Amount += Manu[Order2]

    print(f"Your Payable Amount is {Amount}\nThank You for coming in our Restaurent")

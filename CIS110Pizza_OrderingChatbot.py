print("Hello, my name is Brittany your virtual assistant I will help you order a pizza!")
print("I a going to ask you a few questions. After typing an answer, press Enter.")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name caan not be blank, please enter your name: ")
if userName.lower() == "brittany williams":
    print(f"\nMy Queen, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

size = input("\nWhat size pizza would you like?  [Enter small, medium, or large:  ")
while size.lower() not in ["small", "medium", "large"]:
    size = input("Invalid value, please enter small, medium or large: ")
flavor = input("\nEnter the flavor of pizza:  ")
while len(flavor) == 0:
    flavor = input("Flavor can not be blank, please enter a flavor: ")
crustType = input("\nWhat type of crust do you want:  ")
while len(crustType) == 0:
    crustType = input("Crust type can not be blank, please enter crust type:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized please enter a numerical value: ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery:  ")
while method not in ["carry out", "delivery"]:
    method =  input("Invalid value please enter carry out or delivery: ")
  

                   
if method.lower () == "delivery":
    deliveryFee =  5
else:
    deliveryFee = 0

salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99

 


total = (pizzaCost * quantity) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")

if total >= 50:
    print("\nCongradulations! You just recieved a $10 coupon on your next order!")
else:
    print("\nOrders over $50 will recieve a free $10 dollar off coupon")

print("-" * 10)

# TODO
print("Welcome to Burger Shop!")
size = input("What size Burger do you want? ")
add_mushroom = input("Do you want mushrooms? (Y/N) ")
extra_cheese = input("Do you want extra cheese? (Y/N) ")
final_bill = 0
if size == "M":
    final_bill = 5
    if add_mushroom == "Y":
        final_bill += 1
    if extra_cheese == "Y":
        final_bill += 1
elif size == "N":
    final_bill = 8
    if add_mushroom == "Y":
        final_bill += 1
    if extra_cheese == "Y":
        final_bill += 1
elif size == "L":
    final_bill = 10
    if add_mushroom == "Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1
print(f"Your final bill is: ${final_bill}.") 
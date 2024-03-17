print("Welcome to the Tri Cost Calculator!")
days = int(input("How many days would you stay? "))
cost_per_night = float(input("How much does hotel cost per night? ").replace("$", ""))
flight_cost = float(input("How much does flight cost? ").replace("$", ""))
rental_car = float(input("If you need rental car please enter the price otherwise enter zero. ").replace("$", ""))
other_expenses = float(input("Enter other possible expenses. ").replace("$", ""))

print(" Total Cost: $"+str(days*cost_per_night+flight_cost+rental_car+other_expenses))

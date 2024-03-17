try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    quit()
else:
    pay = hours * rate
    print("Pay: "+str(pay))
finally:
    print("Good Bye!")
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
rate_with_extra =  1.5 if float(hours) > 40 else 0
hours_exttra = float(hours) - 40 if float(hours) > 40 else 0
pay = float(hours) * float(rate) + float(rate_with_extra) * float(hours_exttra)
print("Pay: "+str(pay))
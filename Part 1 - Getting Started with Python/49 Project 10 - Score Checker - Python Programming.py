try:
    score = float(input("Enter score: "))
except ValueError as err:
    print("Bad score")
    quit()
if score < 0.0 or score > 1.0:
    print("Bad score")
else:
    if float(score) >= 0.9:
        print("A")
    elif float(score) >= 0.8:
        print("B")
    elif float(score) >= 0.7:
        print("C")
    elif float(score) >= 0.6:
        print("D")
    else:
        print("F")
def feetToInches(feet: float) -> float:
    return feet * 12


feet = float(input("Enter a number of feet: "))
inches = feetToInches(feet)
print(f"{feet} feet is {inches} inches")

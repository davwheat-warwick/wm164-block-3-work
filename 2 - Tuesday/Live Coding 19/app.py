def poundsToKg(mass):
    POUND_TO_KG = 0.454

    return mass * POUND_TO_KG


lbs = float(input("Enter mass in pounds: "))

print("Mass in kg: ", poundsToKg(lbs))

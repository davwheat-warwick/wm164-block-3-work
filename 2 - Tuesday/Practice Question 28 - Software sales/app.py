COST_PER_UNIT = 99.0


def getDiscount(quantity: int) -> float:
    if quantity < 10:
        return 0
    elif quantity < 20:
        return 0.1
    elif quantity < 50:
        return 0.2
    elif quantity < 100:
        return 0.3
    else:
        return 0.4


quantity = int(input("Enter the number of units purchased: "))

discount = getDiscount(quantity)

subtotal = quantity * COST_PER_UNIT
discountAmount = subtotal * discount
totalAfterDiscount = subtotal - discountAmount

print("Subtotal  :", subtotal)
print("Discount  :", discountAmount)
print("Total cost:", totalAfterDiscount)

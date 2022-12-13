def readNum() -> int:
    num = int(input("Enter a number: "))
    return num


def validateTriangleLengths(side: int, side2: int, side3: int) -> bool:
    # Triangle inequality theorem
    if side + side2 > side3 and side + side3 > side2 and side2 + side3 > side:
        return True
    else:
        return False


side1 = readNum()
side2 = readNum()
side3 = readNum()

validTriangle = validateTriangleLengths(side1, side2, side3)

if validTriangle:
    print("These lengths create a valid triangle.")
else:
    print("These lengths do not create a valid triangle.")

def kineticEnergy(mass: float, velocity: float) -> float:
    return 0.5 * mass * velocity**2


mass = float(input("Enter the mass of the object in kilograms: "))
velocity = float(input("Enter the velocity of the object in meters per second: "))

energy = kineticEnergy(mass, velocity)

print(f"The kinetic energy of the object is {energy} joules.")

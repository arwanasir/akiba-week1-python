name = input(" ")
weight_in_kilograms = float(input(" "))
height_in_meters = float(input(" "))

print("===========================")
print("        BMI REPORT         ")
print("===========================\n")
print(f"Name: {name}")
print(f"Weight: {weight_in_kilograms} kg")
print(f"Height: {height_in_meters} m")
print(f"BMI: {weight_in_kilograms/(height_in_meters**2):.2f}")
print("===========================")


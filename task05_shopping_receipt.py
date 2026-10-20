customer_name = input("name? ")
product_a = input("product name? ")
price_a = float(input("price? "))
quantity_a = int(input("quantity? "))
product_b = input("product name? ")
price_b = float(input("price? "))
quantity_b = int(input("quantity? "))

print("==============================")
print("           RECEIPT            ")
print("==============================")

print(f"\nCustomer: {customer_name}")

print("Product          Price       Qty")
print("--------------------------------")
print(f"{product_a}       {int(price_a)}      {quantity_a}\n")
print(f"{product_b}       {int(price_b)}      {quantity_b}\n")

print(f"Total:    {int((price_a * quantity_a) +(price_b * quantity_b)) } ETB\n")

print("Thank you for shopping!")
print("==============================")

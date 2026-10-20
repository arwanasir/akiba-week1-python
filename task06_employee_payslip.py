employee_name = input("name? ")
basic_salary = int(input("salary? "))
transport_allowance = int(input("transport allowance? ")) 
food_allowance = int(input("food allowance? "))

print("==============================")
print("      EMPLOYEE PAYSLIP ")
print("==============================")

print(f"Employee: {employee_name}")
print(f"Basic Salary:        {basic_salary} ETB")
print(f"Transport Allowance:  {transport_allowance} ETB")
print(f"Food Allowance:       {food_allowance} ETB")
print("------------------------------")
print(f"Gross Salary:        {basic_salary + transport_allowance + food_allowance} ETB")
print("==============================")


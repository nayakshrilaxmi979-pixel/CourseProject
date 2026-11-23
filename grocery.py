def calculate_total(q1, price1, q2, price2):
    total1 = q1 * price1
    total2 = q2 * price2
    total = total1 + total2
    return total

name = input("Enter customer name: ")
phone = input("Enter phone number: ")
bill = input("Enter bill number: ")
date = input("Enter bill date: ")

p1 = input("Enter product 1 name: ")
q1 = int(input("Enter product 1 quantity: "))
price1 = float(input("Enter product 1 price: "))

p2 = input("Enter product 2 name: ")
q2 = int(input("Enter product 2 quantity: "))
price2 = float(input("Enter product 2 price: "))

total1 = q1 * price1
total2 = q2 * price2
total = calculate_total(q1, price1, q2, price2)

print("\n--- Grocery Shop Bill ---")
print("Customer Name:", name)
print("Phone Number:", phone)
print("Bill Number:", bill)
print("Date:", date)
print(p1, ":", total1)
print(p2, ":", total2)
print("Total Amount:", total)

with open("grocery.txt", "a") as f:
    f.write(f"{name}, {phone}, {bill}, {date}, {p1}, {q1}, {price1}, {p2}, {q2}, {price2}, {total}\n")

print("Bill saved successfully!")
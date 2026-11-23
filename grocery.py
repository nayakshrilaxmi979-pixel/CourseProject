import sys

def calculate_total(q1, price1, q2, price2):
    total1 = q1 * price1
    total2 = q2 * price2
    total = total1 + total2
    return total

if __name__ == "__main__":
    name = sys.argv[1]
    phone = sys.argv[2]
    bill = sys.argv[3]
    date = sys.argv[4]

    p1 = sys.argv[5]
    q1 = int(sys.argv[6])
    price1 = float(sys.argv[7])

    p2 = sys.argv[8]
    q2 = int(sys.argv[9])
    price2 = float(sys.argv[10])

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
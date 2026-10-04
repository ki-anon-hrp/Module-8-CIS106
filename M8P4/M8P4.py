# Kirill M8P4 10/03/2026

# Variable for counting extended price and number of orders
extended_price = 0
count_order = 0 

# Open txt file
with open("text.txt") as f:
    lines = f.read().splitlines()

# Header for different conditions
print(f"{'Item':<10} {'Quantity':<10} {'Price':<10} {'Extended Price':<10}")

# Separate data on item, quantity, and price
for i in range(0, len(lines), 3):
    item = lines[i]
    quantity = int(lines[i + 1])
    price = float(lines[i + 2])

# Finding extended price and then store it
    compute_price = quantity * price
    extended_price += compute_price

# Couting number of oders    
    count_order += 1

# Printing all conditions
    print(f"{item:<10} {quantity:<10,.2f} ${price:<10,.2f} ${compute_price:<10,.2f}")

# Finding average order
average = extended_price / count_order

# Printing final statement
print(f"Sum of all the extended prices: ${extended_price:,.2f}")
print(f"Count of orders: {count_order}")
print(f"Average order: ${average:,.2f}")
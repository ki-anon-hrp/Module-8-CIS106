# Kirill M8P3 10/03/2026

# Variable for counting total bonus
total_bonus = 0

# Open txt file
with open("M8P3TEXT.txt") as f:
    lines = f.read().splitlines()

# Separate data on names and salary variables
for i in range(0, len(lines), 2):
    last_name = lines[i]
    salary = float(lines[i + 1])

# Comapring salary with set of numbers for finding rate
    if salary >= 100000:
        rate = 0.2
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.1

# Finding bonus and additing into total bonus
    bonus = salary * rate 
    total_bonus += bonus

# Printing last name, salary, and bonus
    print(f"{last_name:<10} ${salary:<10,.2f} ${bonus:<10,.2f}")

# Printing total bonus
print(f"Total bonus: ${total_bonus:,.2f}")
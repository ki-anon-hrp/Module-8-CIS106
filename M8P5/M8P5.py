# Kirill M8P5 10/03/2026

# Variable for counting tution owed and students amount
tution_owed = 0
students = 0

# Open txt file
with open("text.txt") as f:
    lines = f.read().splitlines()

# Header for different conditions 
print(f"{'Last Name':<10} {'District code':<15} {'Credits':<10} {'Tution Owed':<10}")

# Separate data on last name, distrcit code, credits
for i in range(0, len(lines), 3):
    last_name = lines[i]
    district_code = lines[i+1]
    credits = float(lines[i+2])

# Comparing distrcit code with specific variable and giving specific cost credit
    if district_code == "I":
        cost_credit = 250.00
    else:
        cost_credit = 500.00

# Finding tution cost and then store it
    tution = cost_credit * credits
    tution_owed += tution

# Counting numbers of students 
    students += 1

# Printing all conditions
    print(f"{last_name:<10} {district_code:<15} {credits:<10} ${tution_owed:<10,.2f}")

# Printing final statement
print(f"Sum of all tution: ${tution_owed:,.2f}")
print(f"Number of students: {students}")
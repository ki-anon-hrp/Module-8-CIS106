# Kirill M8P1 10/03/2026

# Entering input
start = input("Start a program Y/N: ")

# Beginning of the loop
while start == "Y":

# Entering princple amount and interest rate
    principle_amount = float(input("Enter principle amount: "))
    interest_rate = float(input("Enter interest rate: "))

# Counting beginning balance and total interest in variables
    beginning_balance = principle_amount
    total_interest = 0

# Printing scheme
    print("\nFormatted output")
    print(f"{'Year':<6}{'Beginning':<15}{'Ending':<15}")
    print(f"{'':<6}{'Balance':<15}{'Balance':<15}")

# For loop for counting interest and adding into total interest
    for year in range(1,6):
        interest = beginning_balance * interest_rate
        ending_balance = beginning_balance + interest
        total_interest += interest 

# Printing beginning and ending balance
        print(f"{year:<6}${beginning_balance:,.2f}{'':<3}${ending_balance:,.2f}")

# Adding ending balance in beginning balance        
        beginning_balance = ending_balance

# Printing total interest
    print(f"\nTotal interest earned: ${total_interest:,.2f}")

# Asking to restart program 
    start = input("Restart a program Y/N: ")

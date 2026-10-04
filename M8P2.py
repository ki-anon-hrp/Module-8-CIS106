# Kirill M8P2 10/03/2026

# Values for starting numbers
first = 1
second = 1

# Printing title
print("First 20 numbers of Fibonacci sequence: ")

# Loop throught values first and second
for i in range(20):
    print(first, end=" ")
    first, second = second, first + second 
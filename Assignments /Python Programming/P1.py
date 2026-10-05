n = int(input("Enter a positive number: "))

total = sum(range(1, n + 1))

print("You entered:", n)
print("The sum of numbers from 1-" + str(n) + " is:", total)

if total % 2 == 0:
    print("The sum (" + str(total) + ") is an EVEN number.")
else:
    print("The sum (" + str(total) + ") is an ODD number.")

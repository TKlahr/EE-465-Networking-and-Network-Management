n = int(input("Enter a positive integer: "))

total = sum(range(1, n + 1))

print("You entered:", n)
print(f"The sum of numbers from 1 to {n} is: {total}")

if total % 2 == 0:
    print(f"The sum ({total}) is an EVEN number.")
else:
    print(f"The sum ({total}) is an ODD number.")

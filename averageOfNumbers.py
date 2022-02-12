# Average of numbers
try:
    num = int(input("How many numbers do you count?: "))
    total = 0

    for n in range(num):
        numbers = float(input("Enter your numbers: "))
        total += numbers

    average = total / num
    print(f"Average of your numbers: {average}")
except ValueError:
    print("""
    Invalid value
    please, Enter valid value
    """)


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a number to calculate the sum of its digits: "))
print(f"The sum of the digits of {number} is: {sum_of_digits(number)}")

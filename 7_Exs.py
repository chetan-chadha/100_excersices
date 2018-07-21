# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line
# def intcheck(no):
#     number = []
#     if no > 0 :
#
#         number.append(no)
def checkDivisibility(digit):
    # If the digit divides the
    # number then return true
    # else return false.
    return (digit % 2 == 0)


# Function to check if
# all digits of n divide
# it or not
def allDigitsDivide(n):
    temp = n
    while (temp > 0):

        # Taking the digit of
        # the number into digit
        # var.
        digit = n % 10
        if ((checkDivisibility(digit)) == False):
            return False

        temp = temp // 10

    return True


# Driver function
numbers = str(input())
items = [int(x) for x in numbers.split(",")]
list = []
for n in items:
    if (allDigitsDivide(n)):
        list.append(n)
    else:
        pass

print(list)

# This code is contributed by Nikita Tiwari.





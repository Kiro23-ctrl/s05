# Input the number
num = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
# Check if the number is divisible by 3
elif num % 3 == 0:
    print("The number is divisible by 3")
# Check if the number is divisible by 5
elif num % 5 == 0:
    print("The number is divisible by 5")
# If not divisible by 3 or 5, print that it's not divisible by either
else:
    print("The number is not divisible by 3 nor 5")
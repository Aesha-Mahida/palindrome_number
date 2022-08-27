num = int(input("Enter the number to be checked: "))
reverse = int(str(num)[::-1])
if reverse == num:
    print("Palindrome number.")
else:
    print("Not Palindrome.")
#Write a program that prompts for an integer number and prints its previous and next numbers.
#Display the results exactly as shown below. There shouldn't be a space before the period.
#Remember that you can convert the numbers to strings using the function 'str'.
n = int(input("Enter Number: "))
add = n+1
sub = n-1
next = "The next number for the number " + str(n) + " is " + str(add) + "."
prev = "The previous number for the number " + str(n) + " is " + str(sub) + "."
print(next)
print(prev)
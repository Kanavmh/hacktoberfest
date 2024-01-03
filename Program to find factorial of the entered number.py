num = int(input("Enter a number: "))
#Initialize the factorial to 1
fac = 1
#Calculate the factorial of the number
for i in range(1, num+1):
  fac *= i
#Print the factorial
print("The factorial of", num, "is", fac)

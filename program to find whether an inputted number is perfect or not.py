def is_perfect(n):
#Initialize sum to 0
  sum = 0
#Find the sum of the divisors of n
  	for i in range(1, n):
    		if n%i == 0:
      		sum += i  
#Return True if sum is equal to n, False otherwise
  return sum == n						                                                   #Get the input from the user
num = int(input("Enter a number: "))
#Check if the number is perfect
if is_perfect(num):
  print(num, "is a perfect number.")
else:
  	print(num, "is not a perfect number.")

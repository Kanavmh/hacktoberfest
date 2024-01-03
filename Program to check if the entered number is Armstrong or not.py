num = int(input("Enter a number: "))
#Initialize sum to 0
sum = 0
#Find the sum of the cubes of the digits of num
temp = num
while temp > 0:
  digit = temp% 10
  sum += digit**3
  temp //= 10
#Check if the sum is equal to num
if num == sum:
  print(num, "is an Armstrong number.")
else:
  print(num, "is not an Armstrong number.")

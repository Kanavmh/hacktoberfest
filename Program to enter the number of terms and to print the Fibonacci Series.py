num = int(input("Enter the number of terms: "))
# Initialize the first two terms
a = 0
b = 1
# Print the first two terms
print(a)
print(b)
# Calculate and print the remaining terms
for i in range(2, num):
  c = a + b
  print(c)
  a = b
  b = c

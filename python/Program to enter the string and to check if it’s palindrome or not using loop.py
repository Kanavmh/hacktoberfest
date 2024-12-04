s = input("Enter a string: ")
# Initialize left and right pointers
left = 0
right = len(s) - 1
# Initialize a flag to track whether the string is a palindrome
is_palindrome = True
# Check if the string is a palindrome
while left < right:
  if s[left] != s[right]:
    is_palindrome = False
    break
  left += 1
  right -= 1
# Print the result
if is_palindrome:
  print(s, "is a palindrome")
else:
  print(s, "is not a palindrome")

#Write a python program to check whether a word reads the same backwards and forwards.
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#write a progrram to accessing string by index

name = "Hello World!"

print("Original strin : ", name)
print("Accessing string by index : ",name[0])  # Accessing first character of
# the string
print("Accessing string by index : ",name[9])  # Accessing last character of
# the string
print("Nagative indexing : ",name[-1])  # Accessing last character of the string
print("Nagative indexing : ",name[-12])  # Accessing first character of the string


print("Nagative indexing : ",name[0:5])  # Accessing character using slice operator 0 to 4
print("Nagative indexing : ",name[:10])  # Accessing character start or stop using slice operator 0 to 9
print("Nagative indexing : ",name[::2])  # Accessing character using slice operator string with step 2
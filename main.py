num = int(input("Enter your original number: "))

# Convert number to binary without '0b'
binary = bin(num)[2:]

# Reverse the binary string
reversed_binary = binary[::-1]

# Convert reversed binary to a new number
new_number = int(reversed_binary, 2)

# Show the results
print("Binary form:", binary)
print("Reversed binary:", reversed_binary)
print("Reversed Number:", new_number)

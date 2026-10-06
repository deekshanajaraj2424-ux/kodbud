# File Reader Program

# Open the text file in read mode
file = open("sample.txt", "r")

# Read the contents of the file
content = file.read()

# Display the contents
print("Contents of the file:")
print(content)

# Close the file
file.close()
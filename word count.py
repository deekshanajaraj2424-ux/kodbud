# Word Count Program

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into individual words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the total word count
print("Total number of words:", word_count)
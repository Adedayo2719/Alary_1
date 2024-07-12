def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize variables to keep track of the longest word and its length
    longest_word = ""
    max_length = 0

    # Iterate through each word in the list
    for word in words:
        # Check if the current word is longer than the previously found longest word
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word

# Example usage:
sentence = "The civil service is hierarchically structured that each higher hierarchy controls others below it."
longest_word = find_longest_word(sentence)
print("Longest word:", longest_word)

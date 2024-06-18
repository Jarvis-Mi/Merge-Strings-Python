# Define a function named `merge_strings` that takes two strings, `word1` and `word2`, as arguments.
def mergeAlternately(self, word1, word2):
  
    """
    Merges two strings by alternating letters, prioritizing word1 and appending 
    remaining characters from the longer word.

    Args:
        word1: The first string.
        word2: The second string.

    Returns:
        The merged string.
    """
  
    # Initialize an empty list to store the merged characters.
    result = []
  
    # Find the maximum length of the two strings.
    max_len = max(len(word1), len(word2))
  
    # Iterate through the range up to the maximum length.
    for i in range(max_len):
        if i < len(word1):  # If the index `i` is within the length of `word1`, append the character at index `i` from `word1` to the `result` list.
            result.append(word1[i])
        if i < len(word2):  # If the index `i` is within the length of `word2`, append the character at index `i` from `word2` to the `result` list.
            result.append(word2[i])
    # Join the characters in the `result` list into a single string and return it.
    return ''.join(result)


# Example usage
word1 = "abc"
word2 = "pqr"
merged_string = merge_strings(word1, word2)
print(f"Merged string: {merged_string}")  # Output: apbqcr

    

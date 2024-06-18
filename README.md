# Merge-Strings-Python
This repository provides a Python function whose main theme is from the following web sub and named 1768.Merge Strings Alternately

[Link text](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75)


# Efficient String Merging in Python

This repository provides a Python function `merge_strings(word1, word2)` that efficiently merges two strings by alternating letters, prioritizing `word1` and appending remaining characters from the longer string.

## Key Features

* Optimized Algorithm: Merges strings efficiently using a minimal loop and direct character access.
* Memory Efficient: Employs minimal data structures and early stopping mechanisms for reduced memory usage.
* Handles Unequal Lengths: Seamlessly handles strings of different lengths, appending remaining characters.

## Example Usage

```python
merged_string = merge_strings("abc", "pqr")
print(merged_string)  # Output: apbqcr

# Suppose you have a list with duplicate elements
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# You can convert it to a set to remove duplicates
# Using dict to remove duplicates and preserve order
dict_without_duplicates = dict.fromkeys(list_with_duplicates)
list_without_duplicates = list(dict_without_duplicates)

print(list_without_duplicates)  # This will output: [1, 2, 3, 4, 5, 6, 7]

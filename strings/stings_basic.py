# Define a sample string
sample_string = "Hello, World!"

# 1. Get the length of the string
string_length = len(sample_string)
print("1. Length of the string is:", string_length)

# 2. Convert the string to uppercase
uppercase_string = sample_string.upper()
print("2. Uppercase:", uppercase_string)

# 3. Convert the string to lowercase
lowercase_string = uppercase_string.lower()
print("3. Lowercase:", lowercase_string)

# 4. Capitalize the string (first character)
capitalized_string = lowercase_string.capitalize()
print("4. Capitalized:", capitalized_string)

# 5. Convert the first character of each word to uppercase
title_case_string = capitalized_string.title()
print("5. Title case:", title_case_string)

# 6. Count the occurrences of a specific character in the string
character_to_count = "l"
character_count = title_case_string.count(character_to_count)
print("6. Count of '{}' in the string: {}".format(character_to_count, character_count))

# 7. Find the index of a substring
substring_to_find = "World"
substring_index = title_case_string.find(substring_to_find)
if substring_index != -1:
    print("7. Index of '{}': {}".format(substring_to_find, substring_index))
else:
    print("7. Substring '{}' not found in the string.".format(substring_to_find))

# 8. Replace occurrences of a substring with another substring
old_substring = "Hello"
new_substring = "Hi"
replaced_string = title_case_string.replace(old_substring, new_substring)
print("8. After replacing '{}':".format(old_substring), replaced_string)

# 9. Split the string into a list of substrings using a separator
separator = ","
split_string = replaced_string.split(separator)
print("9. After splitting using '{}':".format(separator), split_string)

# 10. Remove leading and trailing whitespaces from the string
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print("10. Stripped string:", stripped_string)
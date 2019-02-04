# Write a regular expression that could find invalid characters that you might find in strings. e.g., escape sequences
# to support \, ", and ' and other characters that may not be supported in a regular string variable


import re

# user_string = input('Enter a string to validate: ')
#
# if bool(re.match("[<>/{}[\]~`]", user_string)):
#     print('Your string is NOT Valid')
# else:
#     print('Your String Valid')
print(bool(re.match("[<>/{}[\]~`\"\'\\]", "`string")))
print(bool(re.match("[<>/{}[\]~`\"\'\\]", "string`")))
print(bool(re.match("[<>/{}[\]~`\"\'\\]", "string[]")))
print(bool(re.match("[<>/{}[\]~`\"\'\\]", "[]string")))

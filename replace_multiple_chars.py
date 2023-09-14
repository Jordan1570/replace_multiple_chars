# Replace several characters in a string with other characters
# E.G. Replace "a" with "AA", "e" with "EE", "i" with "II"

# This string:
# 'This is just a string with chars to be replaced'

# becomes:
# 'Th  II  s   II  s just   AA   str  II  ng w  II  th ch  AA  rs to b  EE   r  EE  pl  AA  c  EE  d'

# When 'i' is replaced by '  II  ', 'e' is replaced by '  EE  ', 'a' is replaced by '  AA  '
# 
# # for example

my_string = 'This is just a string with chars to be replaced'
# must be outside of loop so you dont reset the value of the string to '' every iteration
new_string = ''

for a_char in my_string:

    # if char is 'a' concatenate 'AA' to new string etc
    # strings are immutable
    if a_char == 'a':
        new_string += ' AA '
    elif a_char == 'i':
        new_string += ' II '
    elif a_char == 'e':
        new_string += ' EE '
    else:
        # if the char isn't one of the above just concatenate it
        new_string += a_char

print(new_string)
        
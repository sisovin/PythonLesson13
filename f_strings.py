# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
# Closure is a function having access to the scope of its parent
# function after the parent function has returned.

from turtle import title

print("")
title = " Lesson 13: f_strings "
print(f"{title}".upper().center(80, "="))
print("")

title = " # Concatenating Strings # "
print(f"{title}".center(80, "_"))
# Concatenating Strings

person = "Sisovin"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

title = " ### Example: "
print(f"{title}".center(80, "*"))
name = "Sisovin"
age = 52
greeting = f"\nHello, my name is {name} and I am {age} years old.\n"
print(greeting)

title = " # Previous %s formatting # "
print(f"{title}".center(80, "_"))
# Previous %s formatting

message = "\n%s has %s coins left." % (person, coins)
print(message)

title = " # Previous string.format() method # "
print(f"{title}".center(80, "_"))
# Previous string.format() method

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(person, coins)
print(message)

message = "\n{person} has {coins} coins left.".format(
  coins=coins, person=person
)
print(message)

player = {"person": "Sisovin", "coins": 3}

message = "\n{person} has {coins} coins left.".format(**player)

title = " # f-Strings! This is the way. # "
print(f"{title}".center(80, "_"))
# f-Strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)


message = f"\n{player['person']} has {2 * 5} coins left."
print(message)
# %%
print("")
title = " You can pass formatting options "
print(f"{title}".center(80, "_"))
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
    
for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:.2%}")
# %%
print(f"\n2 times {num} is {2 * num:.2f}\n")

for num in range(1, 11):
    print(f"2 times {num} is {2 * num:.2f}")
    
print("")
# Reverse the order for the division results
for num in range(20, 0, -2):
    print(f"{num} divided by 2 is {num / 2:.2f}")

# Left-align
left_aligned = f"{'left':<10}"
print(left_aligned)  # Output: 'left      '

# Right-align
right_aligned = f"{'right':>10}"
print(right_aligned)  # Output: '     right'

# Center-align
center_aligned = f"{'center':^10}"
print(center_aligned)  # Output: '  center  '

# Combining alignment with number formatting
num = 123.456
formatted_num = f"{num:<10.2f}"  # Left-align with 2 decimal places
print(formatted_num)  # Output: '123.46    '

formatted_num = f"{num:>10.2f}"  # Right-align with 2 decimal places
print(formatted_num)  # Output: '    123.46'

formatted_num = f"{num:^10.2f}"  # Center-align with 2 decimal places
print(formatted_num)  # Output: '  123.46  '

print(message)

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)
# %%
print("")
title = " You can pass formatting options "
print(f"{title}".center(80, "_"))
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:<10.2f}\n")  # Left-align

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:>10.2f}")  # Right-align
    
for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:^10.2%}")  # Center-align
# %%
print(f"\n2 times {num} is {2 * num:<10.2f}\n")  # Left-align

for num in range(1, 11):
    print(f"2 times {num} is {2 * num:>10.2f}")  # Right-align
    
print("")
# Reverse the order for the division results
for num in range(20, 0, -2):
    print(f"{num} divided by 2 is {num / 2:^10.2f}")  # Center-align
# %%
print("")
title = " ### Format numbers using f-strings in Python ### "
print(f"{title}".center(80, "*"))
# Format numbers using f-strings in Python

numFormat = 1234.56789

# Fixed-point notation
formatted_num = f"{num:.2f}"
print(formatted_num)  # Output: 1234.57

# Fixed-point notation
formatted_num = f"{numFormat:<10.2f}"  # Left-align
print(formatted_num)  # Output: 1234.57    

# Percentage
percentage = 0.12345
formatted_percentage = f"{percentage:.2%}"
print(formatted_percentage)  # Output: 12.35%

# Percentage
percentage = 0.12345
formatted_percentage = f"{percentage:>10.2%}"  # Right-align
print(formatted_percentage)  # Output:     12.35%

# Thousands separator
large_num = 1234567890
formatted_large_num = f"{large_num:,}"
print(formatted_large_num)  # Output: 1,234,567,890

# Thousands separator
large_num = 1234567890
formatted_large_num = f"{large_num:^15,}"  # Center-align
print(formatted_large_num)  # Output:  1,234,567,890  

# Exponential notation
formatted_exp = f"{num:.2e}"
print(formatted_exp)  # Output: 1.23e+03

# Exponential notation
formatted_exp = f"{numFormat:<10.2e}"  # Left-align
print(formatted_exp)  # Output: 1.23e+03  


# %%
num = 42

# Format with leading zeros to a width of 5
formatted_num = f"{num:05}"
print(formatted_num)  # Output: 00042

# Format with leading zeros and 2 decimal places
num_float = 3.14
formatted_num_float = f"{num_float:08.2f}"
print(formatted_num_float)  # Output: 00003.14
# %%
print(f"{title}".center(80, "_"))
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:010.2f}\n")  # Leading zeros

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:010.2f}")  # Leading zeros

for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:010.2%}")  # Leading zeros
# %%
print(f"\n2 times {num} is {2 * num:010.2f}\n")  # Leading zeros

for num in range(1, 11):
    print(f"2 times {num} is {2 * num:010.2f}")  # Leading zeros

print("")
# Reverse the order for the division results
for num in range(20, 0, -2):
    print(f"{num} divided by 2 is {num / 2:010.2f}")  # Leading zeros
# %%
print("")
title = " ### Format numbers using f-strings in Python ### "
print(f"{title}".center(80, "*"))
# Format numbers using f-strings in Python

numFormat = 1234.56789
# Fixed-point notation
formatted_num = f"{numFormat:010.2f}"  # Leading zeros
print(formatted_num)  # Output: 00001234.57

# Percentage
percentage = 0.12345
formatted_percentage = f"{percentage:010.2%}"  # Leading zeros
print(formatted_percentage)  # Output: 000012.35%

# Thousands separator
large_num = 1234567890
formatted_large_num = f"{large_num:015,}"  # Leading zeros
print(formatted_large_num)  # Output: 0,001,234,567,890

# Exponential notation
formatted_exp = f"{numFormat:010.2e}"  # Leading zeros
print(formatted_exp)  # Output: 001.23e+03
# %%

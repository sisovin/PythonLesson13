# Lesson 13: String Formatting Techniques

This code is a Python script that demonstrates various string formatting techniques, particularly focusing on f-strings. Here's a breakdown of the different sections and what they do: Header and Imports, Title and Concatenating Strings, Example of f-strings, Using f-strings, Formatting Options with f-string, Alignment and Number Formatting, Leading Zeros, More Formatting Examples, Final Formatting Examples.

This script covers a wide range of string formatting techniques in Python, with a strong emphasis on the use of f-strings for readability and efficiency.

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is f_strings in Python?

In Python, f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces `{}`. They are prefixed with an `f` or `F` before the opening quotation mark. F-strings provide a concise and readable way to include the value of Python expressions inside strings.

### Example:

```python
name = "Sisovin"
age = 52
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)
```

### Output:

```
Hello, my name is Alice and I am 30 years old.
```

F-strings were introduced in Python 3.6 and are considered more readable and efficient compared to other string formatting methods like `%` formatting or `str.format()`.

## How can I format numbers using f-strings in Python?

You can format numbers using f-strings in Python by including formatting specifications within the curly braces `{}`. Here are some common formatting options:

1. **Fixed-point notation**: Use `.nf` where `n` is the number of decimal places.
2. **Percentage**: Use `.n%` where `n` is the number of decimal places.
3. **Thousands separator**: Use `,` to include a comma as a thousands separator.
4. **Exponential notation**: Use `.ne` where `n` is the number of decimal places.

### Examples:

```python
num = 1234.56789

# Fixed-point notation
formatted_num = f"{num:.2f}"
print(formatted_num)  # Output: 1234.57

# Percentage
percentage = 0.12345
formatted_percentage = f"{percentage:.2%}"
print(formatted_percentage)  # Output: 12.35%

# Thousands separator
large_num = 1234567890
formatted_large_num = f"{large_num:,}"
print(formatted_large_num)  # Output: 1,234,567,890

# Exponential notation
formatted_exp = f"{num:.2e}"
print(formatted_exp)  # Output: 1.23e+03
```

In your provided code, you are already using some of these formatting options:

```python
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:.2%}")
```

- `{2.25 * num:.2f}` formats the result to 2 decimal places.
- `{num / 4.25:.2%}` formats the result as a percentage with 2 decimal places.

## How can I align the output of f-strings in Python?

You can align the output of f-strings in Python using alignment specifiers within the curly braces `{}`. The alignment options are:

- `<` : Left-align the value.
- `>` : Right-align the value.
- `^` : Center-align the value.

You can also specify a width for the alignment. Here are some examples:

### Examples:

```python
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
```

### Applying to Your Code:

Here is how you can apply alignment to the provided code:

```python
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
formatted_num = f"{numFormat:<10.2f}"  # Left-align
print(formatted_num)  # Output: 1234.57

# Percentage
percentage = 0.12345
formatted_percentage = f"{percentage:>10.2%}"  # Right-align
print(formatted_percentage)  # Output:     12.35%

# Thousands separator
large_num = 1234567890
formatted_large_num = f"{large_num:^15,}"  # Center-align
print(formatted_large_num)  # Output:  1,234,567,890

# Exponential notation
formatted_exp = f"{numFormat:<10.2e}"  # Left-align
print(formatted_exp)  # Output: 1.23e+03
```

## How can I include leading zeros in a formatted number using f-strings in Python?

You can include leading zeros in a formatted number using f-strings in Python by specifying the width of the field and using the `0` character as a fill character. This is done by placing `0` before the width number.

### Example:

```python
num = 42

# Format with leading zeros to a width of 5
formatted_num = f"{num:05}"
print(formatted_num)  # Output: 00042

# Format with leading zeros and 2 decimal places
num_float = 3.14
formatted_num_float = f"{num_float:08.2f}"
print(formatted_num_float)  # Output: 00003.14
```

### Applying to Your Code:

Here is how you can apply leading zeros to the provided code:

```python
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
```

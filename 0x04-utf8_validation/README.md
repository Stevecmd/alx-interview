# 0x04. UTF-8 Validation
For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:
#### Concepts Needed:

1. Bitwise Operations in Python:
- Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<`, `>>`).
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

2. UTF-8 Encoding Scheme:
- Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know Abou- Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

3. Data Representation:
- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.

4. List Manipulation in Python:
- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

5. Boolean Logic:
- Applying logical operations to make decisions within the program.

### Additional Resource
- [Mock Technical Interview](https://www.youtube.com/watch?v=QvqvMxg24gY)

## Tasks
0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

```sh

steve@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

steve@ubuntu:~/0x04-utf8_validation$

steve@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
steve@ubuntu:~/0x04-utf8_validation$

```
File: `0-validate_utf8.py`

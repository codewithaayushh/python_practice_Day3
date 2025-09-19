text = "Hello world"
print(text)

#indexing
print(text[0])  #H
print(text[1])  #e
print(text[2])  #l
print(text[3])  #l
print(text[4])  #o
print(text[5])  #space
print(text[6])  #w
print(text[7])  #o
print(text[8])  #r
print(text[9])  #l
print(text[10]) #d


print(text[-1])  #d


print(text[0:5])  #Hello
print(text[6:11]) #world

print(text[0:11]) #Hello world

#1. Changing Case

# upper()
print(text.upper())   # "HELLO WORLD"

# lower()
print(text.lower())   # "hello world"

# capitalize()
print(text.capitalize())   # "Hello world"

# title()
print(text.title())   # "Hello World"

# swapcase()
print("PyThOn".swapcase())   # "pYtHoN"

# casefold()
print("ß".casefold())   # "ss" (German sharp s → ss)

#2 Searching and finding
# find()
print(text.find("world"))   # 6
print(text.find("Python"))  # -1 (not found)
print(text.find("o"))      # 4 (first occurrence)
print(text.find("o", 5))   # 7 (search from index 5)    
print(text.find("o", 8))   # -1 (not found after index 8)

# rfind()
print(text.rfind("o"))     # 7 (last occurrence)
print(text.rfind("Python")) # -1 (not found)
print(text.rfind("o", 0, 7)) # 4 (search in range 0-7)
print(text.rfind("o", 0, 5)) # 4 (search in range 0-5)
print(text.rfind("o", 0, 4)) # -1 (not found
print(text.rfind("o", 8))    # -1 (not found after index 8)


# 3 testing and checking

# startswith / endswith
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True

# isalpha
print("abc".isalpha())  # True
print("abc123".isalpha())  # False

# isdigit
print("123".isdigit())  # True
print("12.3".isdigit()) # False

# isnumeric
print("²".isnumeric())  # True (Unicode ²)

# isdecimal
print("123".isdecimal())  # True
print("²".isdecimal())    # False

# isalnum
print("abc123".isalnum())  # True

# islower / isupper
print("hello".islower())  # True
print("HELLO".isupper())  # True

# istitle
print("Hello World".istitle())  # True

# isspace
print("   ".isspace())  # True

# isascii
print("Hello".isascii())   # True
print("नमस्ते".isascii())  # False

# isidentifier
print("variable1".isidentifier()) # True
print("1var".isidentifier())      # False

# isprintable
print("Hello".isprintable())   # True
print("\n".isprintable())      # False


#4 replacing and modifiying

txt="Hello world"
print(txt.replace("world", "Python"))  # "Hello Python"
print(txt.replace("o", "w"))            # "HellW wWrld"
print(txt.replace("o", "O", 1))         # "HellO world" (only first occurrence)
print(txt.replace("o", "O", 2))         # "HellO wOrld" (first two occurrences)

# expandtabs
print("hello\tworld".expandtabs(4))  # "hello   world"

# removeprefix
print("python3".removeprefix("python"))  # "3"

# removesuffix
print("hello.py".removesuffix(".py"))   # "hello"


#5 splitting and joining
word="apple,banana,cherry"
#split
print(word.split(","))  # ['apple', 'banana', 'cherry']

#rsplit
print(word.rsplit(",", 1))  # ['apple,banana', 'cherry']

#splitlines
multiline_text = "Hello\nWorld\nPython"
print(multiline_text.splitlines())  # ['Hello', 'World', 'Python']

#join- join a list of strings into a single string with a specified separator
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # "apple, banana, cherry"
print(" - ".join(fruits))  # "apple - banana - cherry"  

#6 whitespace handling
whitespace_text = "   Hello World   "
#strip
print(whitespace_text.strip())  # "Hello World"

#lstrip- strip the left side whitespace
print(whitespace_text.lstrip())  # "Hello World   " 
#rstrip- strip the right side whitespace
print(whitespace_text.rstrip())  # "   Hello World" 

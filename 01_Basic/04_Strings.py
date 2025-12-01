name = "Amin Navabzade"
print(name)

# Strings are Arrays:
print(name[0])
print(name[2])
print(name[10])
print(len(name))

# loop in str:
for i in name:
    print(i, sep=" , ")

# cheking str??:
if "min" in name:
    print("min is in name")
if "x" not in name:
    print("x is not in name")

# Slicing Strings:
print(name[5:12])  # from 5 to 12 (start = 5 , end = 12)
print(name[:8])  # from thr start
print(name[5:])  # to the end
# Negative Indexing: Use negative indexes to start the slice from the end of the string.
print(name[-8:-3])

# Modify Strings:
print(name.upper())
print(name.lower())
name2 = "   Amin Navabzade     "
print(name2.strip()) # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(name.replace("Amin", "Ali")) # "Amin" => "Ali"
a = "a,b,c,d,e"
print(a.split(",")) # The split() method returns a list where the text between the specified separator becomes the list items.

# F-Strings:
age = 22
print(f"I have {age}")
# Placeholders and Modifiers:
print("I have {age}")
# A placeholder can include a modifier to format the value: 
# #                  A modifier is included by adding a colon : followed by a legal formatting type,
# #                         like .2f which means fixed point number with 2 decimals:
price = 20
print(f"The price is {price:.2f} dollars")


# thr other methods: 
"""
capitalize()	Converts the first character to upper case
casefold()   	Converts string into lower case
center()    	Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()   	Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()   	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()  	Returns a translation table to be used in translations
partition() 	Returns a tuple where the string is parted into three parts
replace()    	Returns a string where a specified value is replaced with a specified value
rfind()     	Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()   	Swaps cases, lower case becomes upper case and vice versa
title()     	Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()     	Converts a string into upper case
zfill()      	Fills the string with a specified number of 0 values at the beginning
"""












from ctypes import *

# Interfacing with msvcrt (Miscrosoft Standard C library)
# Printing out time
print(windll.msvcrt.time(None)) # None as a null pointer

windll.msvcrt.puts(b"Hello World in C!")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value = b"AAAAA"
print(mut_str.raw)

# Similar function using memset
windll.msvcrt.memset(mut_str, c_char(b"X"), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)

###

# Load the dll

lib = WinDLL("Dll.dll") #Full path to dll
lib.hello() # Will print from the function hello()

lib.lenght.argtypes = (c_char_p, )
lib.lenght.restype = c_int()

str1 = c_char_p(b"test")
print(lib.lenght(str1))

str2 = c_char_p(b"test1234")
print(lib.lenght(str2)) # will output 8

# We nedd to be aware of the data types when interfacing
# python with c

str3 = b"abc\x00123"
print(len(str3))
print(lib.lenght(c_char_p(str3)))

# Using the add function

lib.add.argtypes = (c_int, c_int)
lib.add.restype = c_int

print("2 + 2 = ",lib.add(2,2)) #calling the add function from the dll

# Using the pointer add function
# Defining our inputs and output
lib.add_p.argtypes = (POINTER(c_int), POINTER(c_int), POINTER(c_int))

# Defining the variables
x = c_int(2)
y = c_int(4)
result = c_int(0)

# Checking our result before using the function
print(result)
print(result.value)

lib.add_p(byref(x), byref(y), byref(result))

print("2 + 2 = ", result.value)
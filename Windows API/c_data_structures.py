from ctypes import *

# creating variables compatible with c

# Boolean
b0 = c_bool(0)
b1 = c_bool(1)

print(b0)
print(type(b0))
print(b0.value)

print(b1)
print(type(b1))
print(b1.value)

# Unsigned integer it will print the maximum value for a 
# 32 bit unsigned integer
i0 = c_uint(-1)
print(i0.value)

# Strings
c0 = c_char_p(b"hola mundo!")
print(c0.value)
print(c0)

# Now change c0 to another value 
c0 = c_char_p(b"Adios mundo!")
print(c0)

# Passing to functions is different we need to use this
# 5 byte buffer initialized with null bytes
p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

# Now changing the value
p0.value = b"a"
print(p0.raw)
# The address will be the same but the value will change
print(p0)

# Pointer instances can be created by calling the pointer function 
# As the name says they point to a specific location of a variable

i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)

print(p0.value)
print(p0)
print(hex(addressof(p0)))

# Reference to p0
pt = byref(p0)
print(pt)

# Cast returns a new instance of a type char pointer that points to pt
# can be used to look at the data stored in the adddress

print(cast(pt, c_char_p).value)

# cast as an integer the value of the string as an integer
print(cast(pt, POINTER(c_int)).contents)
print(ord('a'))

# Recreating the person class as a ctype

class PERSON(Structure):
    _fields_ = [("name", c_char_p), # char_p meands character pointer
                ("age", c_int)]

bob = PERSON(b"bob", 24)

print(bob.name)
print(bob.age)

alice = PERSON(b"alice", 20)
print(alice.name)
print(alice.age)

# Creating arrays/lists is diferent than python
# We need to multiply the data type with the number of elements we want in the array
person_array_t = PERSON * 3 
person_array = person_array_t()

# Adding an entry to the array
person_array[0] = PERSON(b"bob", 24)
person_array[1] = PERSON(b"alice", 20)
person_array[2] = PERSON(b"alex", 21)
# Adding another person is not posible because ther is not enough space

for person in person_array:
    print(person)
    print(person.name)
    print(person.age)
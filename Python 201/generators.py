# A generator function cannot include a return statement 

def generator_demo():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

test = generator_demo()

#Executing this will not start the generator right away
print(test)

# The yield state is rememembered so it will always output the same
# We need to sue the next function
print(next(test)) # Prints 1
print(next(test)) # Prints 2
print(next(test)) # Prints 3

# The loop knows whent to stop when it reaches the stop iteration error
test2 = generator_demo()
for a in test2:
    print(a)

# We can create generator functions with loops
def xor_static_key(a):
    key = 0x5
    for i in a:
        yield chr(ord(i) ^ key)

for i in xor_static_key("ffff"): 
    print(i)

# Anonymous lander expressions ^^REFER TO PYTHON 101^
# Kinda the same as before with other syntax
xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "ffff")

print(xor_static_key2)

for i in xor_static_key2:
    print(i)


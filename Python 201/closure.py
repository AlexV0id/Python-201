def print_out(a):
    print("Outer: {}".format(a))

    def print_in():
        print("Inner: {}".format(a))

    return print_in

# This saves the state of the fucntion including the inner one
test2 = print_out("Hola")

del print_out

# Even if we deleted the function it prints the print in value
test2()

print(print_out("test"))
#!/usr/bin/env python3
def print_fibonacci(length):

    a, b = 0, 1
    fibonacci_sequence = []


    if length == 0:
        pass
    elif length == 1:
        fibonacci_sequence.append(a)
    else:
        while len(fibonacci_sequence) < length:
            fibonacci_sequence.append(a)
            a, b = b, a + b

    print(fibonacci_sequence)



print_fibonacci(2000)









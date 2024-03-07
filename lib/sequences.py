#!/usr/bin/env python3

def print_fibonacci(length):

    if length == 0:
        print("[]")
        return []
    
    elif length == 1:
        print("[0]")
        return [0]
    
    else:
        fibonacci_sequence = [0, 1]  

        while len(fibonacci_sequence) < length:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)

    print(f"{fibonacci_sequence}")
print_fibonacci(9)
"""
Practice and explanation on 'yield' statement in Python.
"""

def yield_practice(): 
    yield 1
    yield 2
    yield 3

def yield_next_square_generator(): 
    i = 1
    while True: 
        yield i*i
        i += 1

def main():
    for i in yield_practice():
        print(i)
    print("----------------------\n")
    for i in yield_next_square_generator():
        if i > 100: break 
        else: print(i)

if __name__ == "__main__":
    main()
print("\n\nFibonacci numbers")
a = 0
b = 1

while a < 20:
    print(a, end=' ')   
    c = a + b
    a = b
    b = c

# same loop but shorter
# The expression on the right side will be evaluated before it goes 
# onto the right side.
print("\n\nFibonacci numbers with different code")
a = 0
b = 1

while a < 20:
    print(a, end=' ')
    a, b = b, a + b

# Even Fibonacci numbers
print("\n\nEven Fibonacci numbers")
a = 0
b = 1

while a < 2000:
    if(a % 2 == 0):
        print(a, end=' ')
    a, b = b, a + b

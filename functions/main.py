# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
# 1.
def greet(name):
    return f'Hello, {name}!'

greeting = greet('Julia')
print(greeting)

# 2.
def add(a, b, c):
    return a + b + c

sum = add(3,7,9)
print(sum)

# 3.
def positive(num):
    return num > 0

is_positive = positive(20)
print(is_positive)

# 4.
def negative(num):
    return num < 0

is_negative = negative(0)
print(is_negative)
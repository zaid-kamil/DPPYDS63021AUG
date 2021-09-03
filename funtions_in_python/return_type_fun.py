def get_message_size():
    msg = input('enter your message')
    return len(msg)

# style 1 -> store and use
size = get_message_size()
print("your message is:",size)

# style 2 -> direct usage
print("your message is:",get_message_size())

# function the returns multiple values
def get_message_size_and_price():
    msg = input('enter your message')
    size = len(msg)
    price = 10 * size
    # return two values, as a tuple
    return size, price

# style 1 -> store and use
output = get_message_size_and_price()
print(output)

# style 2 -> store and use 
s, p = get_message_size_and_price()
print(s)
print(p)

# style 3 -> direct usage
print(get_message_size_and_price())

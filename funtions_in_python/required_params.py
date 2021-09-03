
def adder(a,b,c):
    print(f'{a}+{b}+{c}')
    return a+b+c

# in this function a,b,c are params are required
# if we skip any parameter, then python gives error
result = adder(12,34,5)
print(result)

# throws error
result = adder(12,21,)
print(result)
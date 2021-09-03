# global variable
name = "salmon"
address = "1/2 abc, xyz"

def show():
    # we can accesss global variable
    print("name:", name)
    print("address:", address)

def update_and_show():
    # we can change global variable only we get exclusive access
    global name
    global address
    name = 'Amir'
    address = '2/3 CCC, ZZZ'
    print("name:", name)
    print("address:", address)

print("outside function",name)
print("outside function",address)
show()
update_and_show()
print("outside function",name)
print("outside function",address)

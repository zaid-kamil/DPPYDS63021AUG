# read file
# write to a file
# append to a file
def read(filepath):
    with open(filepath,encoding='utf-8') as f:
        return f.read()

def save_data(filepath, content=''):
    with open(filepath,'w') as f:
        f.write(content)
    print('successfully saved')

def add_data(filepath,content):
    with open(filepath, 'a') as f:
        f.write(content) # append

save_data('happy_feet','movie about a penguin that wants to dance!')
data = read("happy_feet")
add_data('happy_feet','but in the ends every penguin dances')
data = read("happy_feet")
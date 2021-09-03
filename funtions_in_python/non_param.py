# for-else is a loop that can 
# confirm if the loop has completed
# without breaking. The else block of for
# is only executed when the loop completes


def check_prime():
    a = 239
    for i in range(2, a):
        # print(f'{a}/{i}= {a%i}')
        if a % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

def quiz():
    print('enter a aquatic mammal:')
    animal = input("ans:")
    if animal == 'whale' or animal == 'porpoise':
        print('correct')
    else:
        print('incorrect')

    
check_prime()  # calling the function
check_prime()
check_prime()
quiz()
check_prime()


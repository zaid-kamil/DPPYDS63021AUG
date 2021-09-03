# python allows us to pass parameter in 2 formats
# 1. positional parameter
# 2. named parameter

# you can mix both styles, but positional parameters
# are given first and named parameter afterward

def mean(a,b,c,d):
    avg = (a+b+c+d)/4
    return avg

# call styles
m = mean(12,34,56,78) #  positional parameter
print(m)

m = mean(a=12,b=23,c=23,d=13) # named parameter
print(m)

m = mean(b=10,c=2,a=5,d=2) # named parameter
print(m)

m = mean(10,b=5,c=3,d=5) # mix p + n
print(m)

m = mean(12,23,3,d=3)
print(m)
# m = mean(b=10,c=15) # error ->
# print(m)

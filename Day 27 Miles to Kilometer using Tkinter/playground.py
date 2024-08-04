def add(*args):
    sum=0
    print(args[0])
    for n in args:
        sum+=n
    return sum

print(add(1,2,3))

def calculate(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

calculate(add=3,multipl=5)
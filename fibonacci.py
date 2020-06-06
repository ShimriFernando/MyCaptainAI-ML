#fibonacci series

a = int(input("enter a value: "))
b = int(input("enter a value: "))
while (b<150):
    c=a+b
    print(a)
    a = b
    b = c
    c=a+b

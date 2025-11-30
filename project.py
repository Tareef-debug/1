def swap(a,b):
    a = a^b
    b = b^a
    a= a^b
    print("The numbers swapped is a=",a,"b=",b)
a = int(input("Enter your number for  a"))
b = int(input("Enter your number for b"))
def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("The swapped numbers are a =", a,"b =", b)
swap2(1,2)
swap(a,b)
def proize(a,b):
    return a*b
def delet(a,b):
    return a/b
def proverka():
    a = int(input())
    b = int(input())
    c = input("*,/ \n",)
    if c == "*":
        print(proize(a,b))
    elif c == "/":
        print(delet(a,b))

proverka()
print(a)
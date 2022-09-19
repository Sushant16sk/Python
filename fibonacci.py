n=int(input('enter number'))
a=0
b=1
print(a)
print(b)
for i in range(n+1):
    next= a+b
    print(next)
    a=b
    b=next
    
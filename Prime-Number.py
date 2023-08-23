print("Prime Number Checker v1.0")
print("\nBy IntegerSpace06")
print("\n")
a = int(input("Insert number: "))
i=2
booleaz = True
while i<a-1:
    if a%i==0:
        booleaz = False
    i+=1
if booleaz:
    print("Prime number")
else:
    print("Not prime number")

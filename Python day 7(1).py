a = 10
b = 20
c = 30
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greaer than a and c")
else:
        print("c is greater than a and b")


fruits=["Apple","Banana","Avacado"]
if "pineapple" not in fruits:
    print("Pineapple is not in the fruits basket")

#LOOP 

fruits =["Apple","Banana","Avacado","Mango"]
for x in fruits:
    print(x)

for x in range(7):
    print(x)

#While loop
i=1
while i<10:
    print(i)
    i=i+1

#BREAK STATEMENT
A = 0
while True:
    print (A)
    if A >= 5:
        break
    A += 1

#CONTINUE STATEMENT

#LOOPING OVER STRING AND LISTS

L=['EGG','BRAED','MILK']
for x in L:
    print(x)

S1 ="Hello Lily"
for x in S1:
    print (x)
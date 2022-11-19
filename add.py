'''x = int(input("enter a  number:-"))
y = int(input("enter second number:- "))

print(x+y, x*y)'''


import random

arr = []

for i in range(1,20):
    num = random.randint(1,19)
    #.append
    arr.append(num)

print(arr)
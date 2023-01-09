from math import *
#1
for i in range(10):
    print(i, end=",")
print()
#2
for i in range(2,12):
    print(i, end=";")
print()
#3
for i in range(2,12,3):
    print(i, end=" ")
print()
#4
for i in range(12,2,-2):
    print(i,end=" ")
print()
#----------------------
#Примеры использования циклов
#1)
4
print("Arvuta peast! ...4*100-55")

o_vastus=4*100-55

vastus=int(input("Lahenda ülesanne ..."))

k=1

while vastus!=o_vastus:

    print("Viga! Sisesta Õige vastus on ...", )

    vastus=int(input("Sisesta vastus ..."))

    k+=1

print("Õige vastus! Katsed oli ...",k )
print()
#2)

x=0

while x<30:

    if x%2==1:

        print(x, end=" ")

    x+=1
print()
#Использование цикла WHILE TRUE

x=0

while True:

    if x%2==1:

        print(x, end=" ")

    if x== 30:

        break

    x+=1
print()
#Использование цикла FOR

for i in range(1,31,2):

        print(i, end=" ")
#-----------------------------
k=0
while True:
print("Arvuta peast! ...4*100-55")

o_vastus=4*100-55

vastus=int(input("Lahenda ülesanne ..."))

k=1

while vastus!=o_vastus:

    print("Viga! Sisesta Õige vastus on ...", )

    vastus=int(input("Sisesta vastus ..."))

    k+=1

print("Õige vastus! Katsed oli ...",k )
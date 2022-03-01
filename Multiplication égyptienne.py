i = int(input("Choisir un premier nombre : "))
j = int(input("Choisir un deuxième nombre : "))
n = 1
list = []
list.append(n)
while n*2<=i:
    if n <= i:
        n*=2
        list.append(n)

var = 0
list2 = []
for g in reversed(list):
    if g<= i:
        i=i-g
        list2.append(g)

for u in list2:
    var += u*j
print(var)
i = float(input("Choisir un nombre : "))
while i!= 1 :
    if (i%2 == 0):
        i/=2
        print(i)
    else:
        i*=3
        i+=1
        print(i)
#bubble sort
lista_numere=[12 , 34 , 654 , 56 , 90]

def bubble_sort(lista):
    n = len(lista)
    schimbat = True
    while schimbat:
        schimbat = False
        i=0
        while i < n-1:
            if lista[i] > lista[i+1]:
                lista[i] , lista[i+1] = lista[i+1] , lista[i]
                schimbat = True
            i+=1
        print("lista sortata este: ", lista)
bubble_sort(lista_numere)

#functia 3

def cmmmc(a,b):
    produs = a*b
    if produs == 0:
        return "Imposibil"
    else:
        while a != b:
            if a > b:
                a-=b
            else:
                b-=a
        return produs//a

print (cmmmc(4,6))
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [2,       3,        3,       2,        1]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

for index in range(len(elevi)):
    print(f"{elevi[index]} are nota {note[index]}")

nota_minima=min(note)
nota_maxima=max(note)
for i in range(len(elevi)):
    if note[i]==nota_minima:
        print(note[i])
        print(elevi[i])
    elif note[i]==nota_maxima:
        print(note[i])
        print(elevi[i])
suma=sum(note)
print(int(suma/len(note)*100)/100)
for i in range(len(note)):
    if note[i]>=5:
        print (elevi[i])

for i in range(len(note)):
    if note[i]<10:
        note[i]=note[i]+1
elevi.append(elev_nou)
note.append(nota_elev_nou)

pozitie=elevi.index("Darius")
elevi.pop(pozitie)
note.pop(pozitie)
for index in range(len(elevi)):
    print(f"{elevi[index]} are nota {note[index]}")
i=0
while i<len(interogari_nume) and interogari_nume[i]!="stop":
        nume_interogat = interogari_nume[i]
        if nume_interogat in elevi:
            pozitie_catalog = elevi.index(nume_interogat)
            print(note[pozitie_catalog])
        else:
            print("nu exista")
        i=i+1

respinsi=0
promovati=0
for index in range(len(note)):
    if note[i]>=5:
        promovati=promovati+1
    else:
        respinsi=respinsi+1
print(f"{respinsi} elevi respinsi si {promovati} elevi promovati")

note2=[]
for index in range(len(note)):
    if note[i]>=5:
        note2.append(note[i])
if note2==[]:
    print("nu exista")
else:
    print(sum(note2)/len(note2))





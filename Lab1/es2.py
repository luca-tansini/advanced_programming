alkaline_earth_metals=[("barium",56),("beryllium",4),("calcium",20),("magnesium",12),("radium",88),("strontium",38)]

sorted(alkaline_earth_metals, key=lambda a: a[1],reverse=True)[0][1]

alkaline_earth_metals.sort(key=lambda a: a[1])

print("Lista dei metalli sortati: "+str(alkaline_earth_metals)+"\n")

alkaline_earth_metals=dict(alkaline_earth_metals)

noble_gases=dict([("helium",2), ("neon",10), ("argon",18), ("krypton",36), ("xenon",54), ("radon",86)])

tmp = alkaline_earth_metals.copy()
tmp.update(noble_gases)
print("Dizionari Mergiati: "+ str(tmp) +"\n")

#oppure, con l'uso della magia nera, questa espressione restituisce il dizionario joinato senza modificare i primi due
tmp={**alkaline_earth_metals,**noble_gases}

#uso una comprehension
print("Dizionario visto come lista sortata di coppie valore chiave: "+str([ (k,tmp[k])for k in sorted(tmp.keys())])+"\n")

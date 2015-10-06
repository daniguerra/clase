palabras =["abc", "xd", "crm","zl","xb"]


listax = []
listas = []
for palabra in palabras:
	if palabra[0] == "x":
		listax.append(palabra)
	else:
		listas.append(palabra)
		
lista_final = sorted(listax) + sorted(listas)
print lista_final

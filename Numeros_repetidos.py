import pdb
numeros=[1,3,67,67,8,8,5,9,5,3,0,12,12,23,45]

resultado = []



for elemento  in numeros:
	posicion = numeros.index(elemento)
	if posicion != len(numeros) -1:
		if elemento == numeros [posicion+1 ]:
			numeros.remove(elemento)
		
print numeros

resultado = []
for indice,elemento in enumerate(numeros):
	if indice != len(numeros) -1:
		if elemento != numeros[indice+1]:
			resultado.append(elemento)
resultado.append(numeros[-1])
print resultado
		
	
	
	
	

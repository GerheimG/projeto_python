import os


os.system('cls')


valor = int(input("Limite: "))
for numero in range(2, valor + 1):
	soma = 0
	for numero_primo in range(numero):
		numero_primo += 1
		if numero % numero_primo == 0:
			soma += 1
			if numero_primo == numero and soma <= 2:
				print(numero_primo, ",", end=" ")
			elif soma > 2:
				break
import math


def q0():
	print("Olá ETE PORTO DIGITAL!")


def q1():
	ln1 = (input("Digite um numero: "))
	print("O numero escolhido foi: " + ln1)


def q2():
	ln1 = float(input("Digite um numero: "))
	ln2 = float(input("Digite outro numero: "))
	print("a soma dos valores é: " + str(ln1 + ln2))


def q3():
	ln1 = float(input("Digite sua primeira nota do semestre: "))
	ln2 = float(input("Digite sua segunda nota do semestre: "))
	ln3 = float(input("Digite sua terceira nota do semestre: "))
	ln4 = float(input("Digite sua quarta nota do semestre: "))
	print("Sua média semestral é: " + str((ln1 + ln2 + ln3 + ln4) / 4))


def q4():
	ln1 = int(input("Digite o valor em metros: "))
	print(str(ln1) + " metros são equivale a " + str(ln1 * 100) + " centimetros")


def q5():
	raio = float(input("Digite o raio do circulo:"))
	area = math.pi * raio**2
	print("A área do círculo é:", str(area))


def q6():
	raio = float(input("Digite o valor da aresta do quadrado: "))
	area = raio**2
	print("O dobro da área do quadrado é:" + str(area * 2))


def q7():
	valor = float(input("Quanto voce ganha por hora? "))
	horas = float(input("Horas trabalhadas esse mês: "))
	print("Seu salario é:", str(valor * horas))


def q8():
	valor = float(input("digite um valor: "))
	if (valor == 0):
		print("o numero é 0")
	elif (valor > 0):
		print(str(valor) + " é positivo")
	elif (valor < 0):
		print(str(valor) + " é negativo")


def q9():
	letra = (input("Digite uma letra: "))
	if (letra == 'F'):
		print("Sexo Feminino")
	elif (letra == 'M'):
		print("Sexo Masculino")
	else:
		print("Sexo Invalido")


questoes = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9]


def main():
	numb = int(input("Digite o numero da questão desejada(1-10): "))
	questoes[int(numb - 1)]()


main()

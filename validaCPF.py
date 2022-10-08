cpfUsuario = str(input("CPF: "))
cpfCalculo = cpfUsuario[0:9]

multiplicador1 = 10
multiplicador2 = 11
somatorio1 = 0
somatorio2 = 0

for digito in cpfCalculo:
    somador = int(digito) * multiplicador1
    somatorio1 += somador
    multiplicador1 -= 1

calculoDigito1 = 11 - (somatorio1 % 11)

if calculoDigito1 > 9:
    digitoVerificador1 = 0
else:
    digitoVerificador1 = calculoDigito1

cpfNovo = cpfCalculo + str(digitoVerificador1)

for digito in cpfNovo:
    somador = int(digito) * multiplicador2
    somatorio2 += somador
    multiplicador2 -= 1

digitoVerificador2 = 11 - (somatorio2 % 11)

cpfNovo += str(digitoVerificador2)

if cpfNovo == cpfUsuario:
    print(f"CPF Válido!\nDígitos de verificação: {digitoVerificador1}{digitoVerificador2}")

else:
    print(f"CPF Inválido!\nDígitos de verificação: {digitoVerificador1}{digitoVerificador2}")

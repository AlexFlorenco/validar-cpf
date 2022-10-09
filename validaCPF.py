from validateCPF import ValidateCPF

multiplier_1 = 10
multiplier_2 = 11
summation = 0

user_cpf = ValidateCPF(str(input("CPF: ")))

ValidateCPF.check_exception(user_cpf.get_cpf)
analyze_cpf = user_cpf.get_cpf[0:9]

for digit in analyze_cpf:
    adder = int(digit) * multiplier_1
    summation += adder
    multiplier_1 -= 1

verifying_digit_1 = ValidateCPF.calculate_digit(summation)

if verifying_digit_1 > 9:
    verifying_digit_1 = 0

analyze_cpf += str(verifying_digit_1)

summation = 0
for digit in analyze_cpf:
    adder = int(digit) * multiplier_2
    summation += adder
    multiplier_2 -= 1

verifying_digit_2 = ValidateCPF.calculate_digit(summation)

analyze_cpf += str(verifying_digit_2)

if analyze_cpf == user_cpf.get_cpf:
    print(f"CPF Válido!\nDígito Verificador: {verifying_digit_1}{verifying_digit_2}")

else:
    print(f"CPF Inválido!\nDígito Verificador: {verifying_digit_1}{verifying_digit_2}")

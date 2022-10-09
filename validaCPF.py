user_cpf = str(input("CPF: "))
analyze_cpf = user_cpf[0:9]

multiplier_1 = 10
multiplier_2 = 11
sum_1 = 0
sum_2 = 0

for digit in analyze_cpf:
    adder = int(digit) * multiplier_1
    sum_1 += adder
    multiplier_1 -= 1

calculate_digit_1 = 11 - (sum_1 % 11)

if calculate_digit_1 > 9:
    verifying_digit_1 = 0
else:
    verifying_digit_1 = calculate_digit_1

new_cpf = analyze_cpf + str(verifying_digit_1)

for digit in new_cpf:
    adder = int(digit) * multiplier_2
    sum_2 += adder
    multiplier_2 -= 1

verifying_digit_2 = 11 - (sum_2 % 11)

new_cpf += str(verifying_digit_2)

if new_cpf == user_cpf:
    print(f"CPF Válido!\nDígito Verificador: {verifying_digit_1}{verifying_digit_2}")

else:
    print(f"CPF Inválido!\nDígito Verificador: {verifying_digit_1}{verifying_digit_2}")

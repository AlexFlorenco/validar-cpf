class ValidateCPF:
    def __init__(self, cpf):
        self._cpf = cpf

    @property
    def get_cpf(self):
        return self._cpf

    @get_cpf.setter
    def get_cpf(self, new_cpf):
        self._cpf = new_cpf

    @staticmethod
    def calculate_digit(summation):
        return 11 - (summation % 11)

    @staticmethod
    def check_exception(cpf):
        if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8]:
            print('CPF Inválido!')

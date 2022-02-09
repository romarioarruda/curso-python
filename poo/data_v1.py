class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    # Essa função força o retorno de string
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data = Data(19, 7, 1995)
data2 = Data(9, 1, 2022)

print(data)
print(data2)
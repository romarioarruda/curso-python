class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    
    def full_date(self):
        full_month = self.return_full_months(self.mes)

        return f'{self.dia} de {full_month} de {self.ano}'
    
    
    def return_full_months(self, month_number):
        months = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
        }

        return months.get(month_number, "** Mês não reconhecido **")


    # Essa função força o retorno de string
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'



class DataHeranca(Data):
    def __init__(self, dia, mes, ano):
        super().__init__(dia, mes, ano)


data = DataHeranca(1, 2, 2022)
data2 = DataHeranca(1, 1, 2022)

print(data)
print(data2.full_date())
from datetime import date, time, datetime, timedelta


def trabalhando_com_date():

    data_atual = date.today()
    print(data_atual)
    # para formatar a data
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%A %B %Y'))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(type(horario))
    print(horario)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2005, 4, 28, 15, 30, 25)
    print(data_criada)
    nova_data = data_criada - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    # trabalhando_com_time()
    trabalhando_com_datetime()

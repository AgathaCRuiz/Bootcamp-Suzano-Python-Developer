# class datetime.datetime(year, month, day, hour=0, minute=0, second=0,
# microsecond=0, tzinfo=None, *, fold=0)
#    Os argumentos year, month e day são obrigatórios. tzinfo pode ser None, ou uma instância de subclasse de
#    tzinfo. Os argumentos remanescentes devem ser inteiros nos seguintes intervalos:
#
#    • MINYEAR <= year <= MAXYEAR,
#    • 1 <= month <= 12,
#    • 1 <= day <= número de dias no mês e ano fornecidos,
#    • 0 <= hour < 24,
#    • 0 <= minute < 60,
#    • 0 <= second < 60,
#    • 0 <= microsecond < 1000000,
#    • fold in [0, 1].

from datetime import date, time, datetime

# Date - YYYY-MM-DD
data = date(2023, 7, 10)
print(data)
print(date.today())

# Time - HH:MM:SS
hora = time(10,30, 20)
print(hora)
print(datetime.now().time())

# Datetime - YYYY-MM-DD HH:MM:SS
data_hora = datetime(2023, 7, 10)
print(data_hora)
data_hora = datetime(2023, 7, 10, 10, 30, 20)
print(data_hora)
print(datetime.today())
# Trabalhando com Datas e Tempos em Python

## 1. Módulo `datetime`

O módulo `datetime` em Python fornece classes para manipulação de datas e horários de maneira eficiente e intuitiva.

### 1.1 Principais Classes

```python
from datetime import date, time, datetime, timedelta, timezone
```

- **date**: Representa uma data (ano, mês, dia)
- **time**: Representa um horário (hora, minuto, segundo, microssegundo)
- **datetime**: Combina data e horário
- **timedelta**: Representa uma duração ou diferença entre datas/horários
- **timezone**: Representa informações de fuso horário (Python 3.2+)

## 2. Classe `datetime.datetime`

```python
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

### 2.1 Parâmetros

- **year, month, day**: Obrigatórios
- **hour, minute, second, microsecond**: Opcionais (default: 0)
- **tzinfo**: Opcional, para informações de fuso horário
- **fold**: Opcional, usado para resolver ambiguidades durante mudanças de horário de verão

### 2.2 Intervalos Válidos

- `MINYEAR <= year <= MAXYEAR`
- `1 <= month <= 12`
- `1 <= day <= número de dias no mês e ano fornecidos`
- `0 <= hour < 24`
- `0 <= minute < 60`
- `0 <= second < 60`
- `0 <= microsecond < 1000000`
- `fold in [0, 1]`

### 2.3 Métodos comuns

```python
# Obter data e hora atual
datetime.now()      # Data e hora local com timezone se especificado
datetime.today()    # Data e hora local, sempre sem timezone
datetime.utcnow()   # Data e hora UTC, sem timezone

# Parsing e formatação
datetime.strptime("21/05/2023", "%d/%m/%Y")  # String para datetime
data_hora.strftime("%d/%m/%Y %H:%M")         # Datetime para string formatada
```

### 2.4 Atributos

```python
dt = datetime.now()
dt.year         # Ano
dt.month        # Mês
dt.day          # Dia
dt.hour         # Hora
dt.minute       # Minuto
dt.second       # Segundo
dt.microsecond  # Microssegundo
dt.tzinfo       # Informação de timezone (ou None)
dt.fold         # Valor de fold (0 ou 1)
```

## 3. Classe `datetime.date`

Representa uma data no calendário gregoriano.

```python
# Criação
data = date(2023, 7, 10)
hoje = date.today()

# Atributos
data.year   # Ano
data.month  # Mês
data.day    # Dia

# Métodos comuns
data.weekday()     # Dia da semana (0=Segunda, 6=Domingo)
data.isoweekday()  # Dia da semana ISO (1=Segunda, 7=Domingo)
data.isoformat()   # String ISO8601 (YYYY-MM-DD)
data.replace(year=2024)  # Novo objeto com o ano alterado
```

## 4. Classe `datetime.time`

Representa um horário, independente de qualquer data específica.

```python
# Criação
hora = time(10, 30, 45, 500)  # 10:30:45.000500

# Atributos
hora.hour        # Hora
hora.minute      # Minuto
hora.second      # Segundo
hora.microsecond # Microssegundo
hora.tzinfo      # Timezone (ou None)
hora.fold        # Fold (0 ou 1)

# Métodos comuns
hora.isoformat()  # String ISO8601 (HH:MM:SS.mmmmmm+HH:MM)
hora.replace(hour=11)  # Novo objeto com a hora alterada
```

## 5. Classe `datetime.timedelta`

Representa uma duração ou diferença entre datas e/ou horários.

### 5.1 Criação

```python
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

Todos os parâmetros são opcionais e podem ser inteiros ou floats, positivos ou negativos.

### 5.2 Normalização

Internamente, `timedelta` normaliza os argumentos para três valores:

- **days** (dias inteiros)
- **seconds** (0 a 86399)
- **microseconds** (0 a 999999)

### 5.3 Atributos

```python
td = timedelta(days=2, hours=3)
td.days          # Dias inteiros
td.seconds       # Segundos (0-86399)
td.microseconds  # Microssegundos (0-999999)
td.total_seconds()  # Total da duração em segundos (float)
```

### 5.4 Operações

```python
# Adição e subtração com datetime
hoje = datetime.now()
amanha = hoje + timedelta(days=1)
ontem = hoje - timedelta(days=1)

# Operações entre timedeltas
td1 = timedelta(days=2)
td2 = timedelta(hours=36)
td_soma = td1 + td2        # 3 dias e 12 horas
td_diff = td1 - td2        # 0 dias e 12 horas
td_multi = td1 * 2         # 4 dias
td_div = td1 / 2           # 1 dia
proporcao = td1 / td2      # Proporção (float)

# Valores absolutos e negação
abs(timedelta(days=-5))    # 5 dias
-timedelta(days=3)         # -3 dias
```

### 5.5 Constantes

```python
timedelta.min       # Menor valor: timedelta(-999999999)
timedelta.max       # Maior valor: timedelta(days=999999999, hours=23, minutes=59, seconds=59...)
timedelta.resolution  # Menor diferença possível: timedelta(microseconds=1)
```

## 6. Exemplos Práticos

### 6.1 Formatação de datas

```python
from datetime import datetime

agora = datetime.now()
print(f"Data formatada: {agora.strftime('%d/%m/%Y')}")
print(f"Data e hora: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Nome do mês: {agora.strftime('%B')}")
print(f"Dia da semana: {agora.strftime('%A')}")
```

### 6.2 Parsing de strings

```python
data_texto = "21/05/2023 14:30:45"
data_objeto = datetime.strptime(data_texto, "%d/%m/%Y %H:%M:%S")
print(f"String convertida: {data_objeto}")
```

### 6.3 Cálculos com datas

```python
from datetime import date, timedelta

hoje = date.today()
amanha = hoje + timedelta(days=1)
proxima_semana = hoje + timedelta(weeks=1)
ha_cinco_dias = hoje - timedelta(days=5)

# Diferença entre datas
data1 = date(2023, 1, 1)
data2 = date(2023, 12, 31)
diferenca = data2 - data1
print(f"Diferença em dias: {diferenca.days}")
```

### 6.4 Calculando idade

```python
from datetime import date

def calcular_idade(nascimento):
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

data_nascimento = date(1990, 5, 15)
idade = calcular_idade(data_nascimento)
print(f"Idade: {idade} anos")
```

### 6.5 Trabalhando com fusos horários

```python
from datetime import datetime, timezone, timedelta
import pytz  # biblioteca adicional

# UTC
agora_utc = datetime.now(timezone.utc)

# Timezone com offset fixo
tz_brasil = timezone(timedelta(hours=-3))
agora_brasil = datetime.now(tz_brasil)

# Usando pytz para timezones com nomes
sp_tz = pytz.timezone('America/Sao_Paulo')
hora_sp = datetime.now(sp_tz)

# Converter entre timezones
hora_sp = sp_tz.localize(datetime.now())
hora_ny = hora_sp.astimezone(pytz.timezone('America/New_York'))
```

### 6.6 Tempo até um evento

```python
from datetime import datetime, timedelta

# Data atual
hoje = datetime.now()

# Data do evento (próximo Ano Novo)
proximo_ano = hoje.year + 1 if hoje.month == 12 and hoje.day > 25 else hoje.year
natal = datetime(proximo_ano, 12, 25, 0, 0, 0)

# Cálculo do tempo restante
tempo_restante = natal - hoje

# Formatar resultado
dias = tempo_restante.days
horas = tempo_restante.seconds // 3600
minutos = (tempo_restante.seconds % 3600) // 60
segundos = tempo_restante.seconds % 60

print(f"Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o Natal")
```

### 6.7 Duração de um processo

```python
from datetime import datetime

# Início da operação
inicio = datetime.now()

# Operação a ser medida
for i in range(1000000):
    pass

# Fim da operação
fim = datetime.now()

# Cálculo da duração
duracao = fim - inicio
print(f"A operação levou {duracao.total_seconds():.6f} segundos")
```

### 6.8 Encontrando datas especiais

```python
from datetime import date, timedelta
import calendar

def proximo_dia_semana(dia_semana):
    """Retorna a data do próximo dia da semana (0=segunda, 6=domingo)"""
    hoje = date.today()
    dias_ate = (dia_semana - hoje.weekday()) % 7
    if dias_ate == 0:  # Se hoje for o dia desejado, pega o próximo
        dias_ate = 7
    return hoje + timedelta(days=dias_ate)

# Próximo domingo
print(f"Próximo domingo: {proximo_dia_semana(6)}")

# Último dia do mês atual
def ultimo_dia_do_mes(ano, mes):
    _, ultimo_dia = calendar.monthrange(ano, mes)
    return date(ano, mes, ultimo_dia)

hoje = date.today()
print(f"Último dia do mês atual: {ultimo_dia_do_mes(hoje.year, hoje.month)}")
```

## 7. Formato de Data/Hora (strftime e strptime)

| Diretiva | Significado                                     | Exemplo                |
| -------- | ----------------------------------------------- | ---------------------- |
| `%a`     | Dia da semana abreviado                         | Sun, Mon, ...          |
| `%A`     | Dia da semana completo                          | Sunday, Monday, ...    |
| `%w`     | Dia da semana como número (0=domingo)           | 0, 1, ..., 6           |
| `%d`     | Dia do mês (01-31)                              | 01, 02, ..., 31        |
| `%b`     | Mês abreviado                                   | Jan, Feb, ...          |
| `%B`     | Mês completo                                    | January, February, ... |
| `%m`     | Mês como número (01-12)                         | 01, 02, ..., 12        |
| `%y`     | Ano sem século (00-99)                          | 00, 01, ..., 99        |
| `%Y`     | Ano com século                                  | 2023, 2024, ...        |
| `%H`     | Hora (00-23)                                    | 00, 01, ..., 23        |
| `%I`     | Hora (01-12)                                    | 01, 02, ..., 12        |
| `%p`     | AM/PM                                           | AM, PM                 |
| `%M`     | Minuto (00-59)                                  | 00, 01, ..., 59        |
| `%S`     | Segundo (00-59)                                 | 00, 01, ..., 59        |
| `%f`     | Microssegundo (000000-999999)                   | 000000, ..., 999999    |
| `%z`     | Offset UTC                                      | +0000, -0400, +1030    |
| `%Z`     | Nome do timezone                                | UTC, EST, CST          |
| `%j`     | Dia do ano (001-366)                            | 001, 002, ..., 366     |
| `%U`     | Semana do ano (00-53) domingo como primeiro dia | 00, 01, ..., 53        |
| `%W`     | Semana do ano (00-53) segunda como primeiro dia | 00, 01, ..., 53        |
| `%c`     | Representação de data e hora local              | Depende da localidade  |
| `%x`     | Representação de data local                     | Depende da localidade  |
| `%X`     | Representação de hora local                     | Depende da localidade  |
| `%%`     | Um caractere % literal                          | %                      |

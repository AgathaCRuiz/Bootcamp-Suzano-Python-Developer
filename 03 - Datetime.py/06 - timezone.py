from datetime import datetime, timezone, timedelta

# Criando datetime com timezone
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(d)

# Convertendo para outro timezone
d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)

# mas sobre timezone
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_sp)
funcionarios = [
    {'nome': 'Abraao', 'salario': 1200},
    {'nome': 'Gisele', 'salario': 1700}
]

def fn(item: dict):
    return item.get('salario')

salarios = map(fn, funcionarios)

for s in salarios:
    print(s) 
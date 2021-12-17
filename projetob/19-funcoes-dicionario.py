def calcular(kwargs):
    v1 = kwargs.get('valor1')
    v2 = kwargs.get('valor2')
    op = kwargs.get('operacao')
    conta = '{} {} {}'.format(v1, op, v2)
    return eval(conta)


resul = calcular(valor1=10, valor2=12, operacao='+')
p = {
    'valor1': 22,
    'valor2': 15,
    'operacao': '-'
}
print(resul)
print(calcular(p))

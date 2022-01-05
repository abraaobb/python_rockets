def receber_funcionario():
    nome = input('digite o nome: ')
    sexo = input('digite o sexo: ')
    salario = float(input('digite o salario: '))
    dados = {'nome': nome, 'sexo': sexo, 'salario': salario}
    return dados


funcionarios = []
while True:
    op = int(input('''0 - sair
1 - inserir funcionario
2 - somar salarios
digite a opcao: 
'''))
    if op == 0:
        print('fim do programa')
        break
    elif op == 1:
        funcionario = receber_funcionario()
        funcionarios.append(funcionario)
    elif op == 2:
        salarios = [f.get('salario') for f in funcionarios]
        print('a soma dos salarios é: {}'.format(sum(salarios)))

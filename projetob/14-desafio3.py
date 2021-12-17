# Criar um programa para adicionar funcionários. Os funcionários devem ter nome, sexo e salário o programa
# deve retornar a soma de salários dos homens e soma dos salários das mulheres
funcionario_model = {
    'nome': None,
    'sexo': None,
    'salario': None
}

funcionarios = list()
soma_masculino = 0
soma_feminino = 0

while True:
    op = int(input('''[1] - inserir funcionario
[2] - soma de salarios dos homens
[3] - soma de salarios dos mulheres
[4] - listar funcionarios
[0] - sair
digite a opcao: '''))
    if op == 0:
        print('fim do programa')
        break
    elif op == 1:
        funcionario = funcionario_model
        funcionario['nome'] = input('digite o nome do funcionario: ')
        print('M - Masculino')
        print('F - Feminino')
        funcionario['sexo'] = input('digite o sexo: ')
        funcionario['salario'] = float(input('digite o salario: '))
        if funcionario.get('sexo') == 'M':
            soma_masculino += funcionario.get('salario', 0)
        else:
            soma_feminino += funcionario.get('salario', 0)
        funcionarios.append(funcionario)
        print(funcionarios)
        print(funcionario)
    elif op == 2:
        print('salario dos homens: {}'.format(soma_masculino))
    elif op == 3:
        print('salario das mulheres: {}'.format(soma_feminino))
    elif op == 4:
        for f in funcionarios:
            print(f)
    else:
        print('opcao invalida')

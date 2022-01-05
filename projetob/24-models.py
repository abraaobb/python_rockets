class Aplicacao:
    def exibir_menu():
        print('1 - cadastrar')
        print('2 - listar todos')
        print('3 - somar salario homens')
        print('4 - somar salario mulheres')
        print('0 - sair')
        op = int(input('digite a opção desejada: '))
        return op


class BancoDados:
    def salvar_arquivo():
        pass

    def ler_arquivo():
        pass


class Funcionario:
    def __init__(self, nome, salario, sexo) -> None:
        self.nome = nome
        self.salario = salario
        self.sexo = sexo

if op == 1:
    pass
elif op == 2:
    pass
elif op == 3:
    pass
elif op == 4:
    pass
elif op == 0:
    pass
else:
    print('opção inválida')
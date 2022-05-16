from Funcionario import Funcionario

nome = input('Qual o nome do funcionário?\n')

profissao = input('Qual a profissão do funcionário?\n')

salario = float(input('Qual o salário do funcionário?\n'))

funcionario = Funcionario(nome, profissao, salario)

funcionario.NomeSet(nome)

funcionario.ProfissaoSet(profissao)

funcionario.SalarioBaseSet(salario)

def informacoes():
  print('Nome: ', funcionario.NomeGet(), '\nProfissão: ',  funcionario.ProfissaoGet(), '\nSalário Base: ', funcionario.SalarioBaseGet())

informacoes()

reajuste = int(input('Qual o reajuste?\n'))

funcionario.SalarioBaseSet(funcionario.Reajuste(funcionario.SalarioBaseGet(), reajuste))

informacoes()
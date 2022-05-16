class Funcionario(object):
  
  def __init__(self, nome, profissao, salarioBase):
        self.__nome = nome
        self.__profissao = profissao
        self.__salarioBase = salarioBase


  def NomeGet(self):
        return self.__nome

  def NomeSet(self, nome):
        self.__nome = nome
    
  def ProfissaoGet(self):
        return self.__profissao

  def ProfissaoSet(self, profissao):
        self.__profissao = profissao
   

  def SalarioBaseGet(self):
        return self.__salarioBase

  def SalarioBaseSet(self, salarioBase):
        self.__salarioBase = salarioBase
    
  def Reajuste(self, salarioBase, reajuste):
    aumento = salarioBase*(reajuste/100)
    salarioAtual = salarioBase + aumento
    return salarioAtual

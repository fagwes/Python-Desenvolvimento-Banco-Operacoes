loc = input('Escolha a Operação: ')

Saldo = 1500
Saque = 400
Deposito = 200
Transferencia = 100

#SALDO#
if loc == 'Saldo':
    print('Saldo em Conta:',Saldo,)

#SAQUE#
elif loc == 'Saque':
    print('Valor Solicitado de Saque:',Saque,)
    print('Operação Realizada com Sucesso:')
    print('Saldo em Conta:',Saldo-Saque)

#DEPOSITO#

elif loc == 'Deposito':
    print('Valor de Deposito Realizado:',Deposito,)
    print('Operação Realizada com Sucesso:')
    print('Saldo em conta:',Saldo+Deposito)

#TRANSFERENCIA#

elif loc == 'Transferencia':
    print('Valor de Transferencia Realizada:', Transferencia, )
    print('Operação Realizada com Sucesso:')
    print('Saldo em conta:', Saldo - Transferencia)

else:
    print('Digite uma Operação')
    
################################################################################################################################

#EXEMPLO 2, ADICIONANDO UM INPUT PARA QUE O USUÁRIO INSIRA UM VALOR:

loc = input('Escolha a Operação: ')
valor = int(input('Digite o valor:'))

Saldo = 1500
Saque = valor
Deposito = valor
Transferencia = valor

#SALDO#
if loc == 'Saldo':
    print('Saldo em Conta:',Saldo,)

#SAQUE#
elif loc == 'Saque':
    print('Valor Solicitado de Saque:',valor,)
    print('Operação Realizada com Sucesso:')
    print('Saldo em Conta:',Saldo-valor)

#DEPOSITO#

elif loc == 'Deposito':
    print('Valor de Deposito Realizado:',valor,)
    print('Operação Realizada com Sucesso:')
    print('Saldo em conta:',Saldo+valor)

#TRANSFERENCIA#

elif loc == 'Transferencia':
    print('Valor de Transferencia Realizada:', valor, )
    print('Operação Realizada com Sucesso:')
    print('Saldo em conta:', Saldo - valor)

else:
    print('Digite uma operação')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

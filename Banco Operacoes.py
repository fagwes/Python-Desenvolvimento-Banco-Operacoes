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

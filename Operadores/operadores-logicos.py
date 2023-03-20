#AND = para ser True tudo tem que ser True
#OR = para ser False tudo tem que ser False

print (True and True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)

# exemplo de uma conta bancária com saldo e limite de saque 
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_espercial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_espercial_com_saldo_suficiente
print(exp_3)



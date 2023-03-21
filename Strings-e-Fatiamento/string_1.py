nome = "Guilherme"

print(nome.upper()) # deixar tudo maiúsculo
print(nome.lower()) # deixar tudo minúsculo
print(nome.title()) # deixar a primeira letra maiúscula

texto = "  Olá, mundo!    "

print(texto + ".") 
print(texto.strip() + ".") # remover espaços em branco 
print(texto.rstrip() + ".") # remover espaços em branco da direita
print(texto.lstrip() + ".") # remover espaços em branco da esquerda

menu = "Python"

print("###" + menu + "###")
print(menu.center(14)) # centralizar
print(menu.center(14, "#")) # centralizar com um caractere 
print("P-y-t-h-o-n")
print("-".join(menu)) 



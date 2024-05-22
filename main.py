#Crie um programa que receba um texto de um usuário e imprima quantas vogais
#[a,e,i,o,u] ele tem.

texto = str(input("Digite um texto: "))
vogais = 0

for i in texto.lower():
    if i in 'aeiou':
        vogais += 1
print("o texto contem: ", vogais, "vogais.")
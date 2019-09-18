letras = input('[ * ] Caracteres Presentes: ')
quantidade = int(input('[ * ]Quantidade de Caracteres: '))
nome = input('[ * ] Nome do arquivo de saida: ')
senha = [letra for letra in letras]
for x in range(quantidade-1):
    senha = [letra+seq for letra in letras for seq in senha]

arquivo = open(nome, 'w')
for x in senha:
    arquivo.write(x+'\n')

arquivo.close()
print('[ *** ] WORDLIST GERADA COM SUCESSO!')
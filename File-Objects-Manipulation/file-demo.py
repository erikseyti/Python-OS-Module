
# metodo não recomendado para manipular arquivos.
# pois é necessario fechar o arquivo uma vez aberto para evitar erros no sistema.
f = open('text.txt', 'r')

# Indica o nome do arquivo a ser aberto.
print(f.name)

# Indica qual foi o metodo no qual o arquivo foi aberto.
print(f.mode)

# Fecha a conexão com o arquivo.
f.close()

# Abrindo arquivos utilizando um File Manager.
# uma das vantagens de se fazer uso desse metodo em manipular arquivos:
# Uma vez que bloco de codigo estiver finalizado, a conexão com o arquivo é fechado aautomaticamente.
with open('text.txt', 'r') as f:
    # f_contents = f.read()
    # # Imprimi todo o conteudo do nosso arquivo text.txt;
    # # Meio recomendado apenas para arquivos com pouco texto.
    # print(f_contents)

    #
    f_lines = f.readlines()
    print(f_lines)


# indica para nós que o arquivo esta realmente fechado.
# retona o valor Booleano: True.
print(f.closed)

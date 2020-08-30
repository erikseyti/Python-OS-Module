import os
from datetime import datetime

# print(dir(os))

# nos passa o caminho atual onde o arquivo esta no sistema.
print(os.getcwd())

# troca o caminho onde o arquivo do python, deve ser executado.
# neste caso, ele trocou o path padrão, onde esta o arquivo, pela pasta tmp dentro do ubuntu.
os.chdir('/tmp')

print(os.getcwd())
# retona uma lista dos arquivos presentes de um determinado diretorio.
# print(os.listdir())

# Cria uma nova pasta dentro daquele diretorio onde esta rodando o processo.
os.mkdir("Teste1")

# Cria uma nova pasta dentro daquele diretorio onde esta rodando o processo, a diferença é que podemos tambem criar subpastas dessa forma.
os.makedirs("primeiroDiretorio/Teste2")

# Exclui uma nova pasta dentro daquele diretorio onde esta rodando o processo.
os.rmdir("Teste1")
# Exclui uma nova pasta dentro daquele diretorio onde esta rodando o processo, a diferença é que podemos tambem excluir subpastas dessa forma.
os.removedirs('primeiroDiretorio/Teste2')

# Funcionalidade que renomeia um arquivo presente dentro daquele diretório onde está sendo rodado o processo do python.
# caso o arquivo não exista irá exibir um erro.
# os.rename("text",'demo.txt')

# Exibe diversos dados a respeito do arquivo que foi criado.
print(os.stat('demo'))

print(os.stat('demo').st_size)

modtime = os.stat('demo').st_mtime
print(datetime.fromtimestamp(modtime))

# print(os.listdir())

for dirpath, dirnames, filenames in os.walk('/tmp'):
    print(f'Diretorio do Path {dirpath}')
    print(f'Diretorio {dirnames}')
    print(f'Arquivos {filenames}')
    print()

# Exibe o caminho até o path "HOME"
print(os.environ.get('HOME'))

# iremos a seguir criar um arquivo chamado "test.txt" para o path na HOME do usuario.
'test.txt'

# não fazer dessa forma para criar o arquivo no path HOME
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

#fazer dessa forma para criar o arquivo no path HOME
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

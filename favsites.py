#!/usr/bin/env Python

# Imports necessários ao projeto
import sys
import json
import webbrowser

# Mensagem de Entrada
index = """
 ____    _   _   ____    _____   _   _ 
|  _ \  | | | | | __ )  | ____| | \ | |
| |_) | | | | | |  _ \  |  _|   |  \| |
|  _ <  | |_| | | |_) | | |___  | |\  |
|_| \_\  \___/  |____/  |_____| |_| \_|
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Script que abre sites favoritos pré-configurados num ficheiro txt
Desenvolvido por: Rúben Silva
GitHub: rubenandre
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

# Obtém o nº total de argumentos escritos no shell
argumentos = sys.argv
# Coloca o primeiro argumento como o nome do ficheiro
favsitesScript = argumentos[0]
urls = []
# Verifica se tem 3 argumentos, os necessários à execução do script
if len(argumentos) == 3:
    # Segundo argumento é a tag --sites
    argumentos[1] = "--sites"
    # Lista de sites vai ser o terceiro argumento
    lista = argumentos[2]
    # Verifica se o ficheiro é do tipo .txt
    if ".txt" not in lista:
        print("Extensao .txt obrigatoria")
        exit()
    # É aberto o arquivo e lidas todas as linhas do mesmo
    try:
        abrir = open(lista, 'r')
        sites = abrir.readlines()
    except:
        print("Nao consegui abrir o " + lista + ".")
# Mensagem de erro
else:
    print('Use: python3' + favsitesScript + '--arquivo shell.txt --lista sites.txt')
    exit()

print(index)
# São abertos os sites
for url in sites:
    webbrowser.open(url)

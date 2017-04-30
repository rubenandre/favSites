#!/usr/bin/env Python

import sys
import json
import webbrowser
index = """
 ____    _   _   ____    _____   _   _ 
|  _ \  | | | | | __ )  | ____| | \ | |
| |_) | | | | | |  _ \  |  _|   |  \| |
|  _ <  | |_| | | |_) | | |___  | |\  |
|_| \_\  \___/  |____/  |_____| |_| \_|
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Scrypt que abre sites favoritos pre-configurados num ficheiro txt
Escrito por: Ruben Silva
GitHub: rubenandre
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""

argumentos = sys.argv
favsitesScript = argumentos[0]
urls = []
if len(argumentos) == 3:
    argumentos[1] = "--sites"
    lista = argumentos[2]
    if ".txt" not in lista:
        print("Extensao .txt obrigatoria")
        exit()
    try:
        abrir = open(lista, 'r')
        sites = abrir.readlines()
    except:
        print("Nao consegui abrir o " + lista + ".")

else:
    print('Use: python3' + favsitesScript + '--arquivo shell.txt --lista sites.txt')
    exit()

print(index)
for url in sites:
    webbrowser.open(url)

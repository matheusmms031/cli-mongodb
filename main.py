import pymongo
import os
# Entra no site do MongoDB Atlas e copie o que foi dado
# entre os parenteses do MongoClient()
client = pymongo.MongoClient("<DIGITE AQUI A SENHA E USUARIO E IP PARA SE CONNECTAR>")

def search_data(collection):
    vals = collection.__dict__
    for key in vals.keys():
        if key == '_Collection__database':
            results = collection.find()
            print("")
            print("     | Values")
            print("     ----------------------------------")
            print("")
            for result in results:
                print(f"         {result}")
            print("")
            print("     -----------------------------------")
            print("     |")
            print("")
        if key == '_Database__name':
            results = collection.list_collection_names()
            print("")
            print("     | Collections")
            print("     ----------------------------------")
            print("")
            for result in results:
                print(f"         {result}")
            print("")
            print("     -----------------------------------")
            print("     |")
            print("")

def inicio():
    print("""
+--------------------------------------+
|                                      |
|            Banco de dados            |
|               MongoDB                |
|                 1.0                  |
|            m4theww#7204              |
|                                      |
+--------------------------------------+""")

inicio()
db = ''
while True:
    command = str(input("[x]> "))
    dicionario = {}
    lista = command.strip().split(" ")

    if command.startswith("select-db"):
        if lista[1] in client.list_database_names():
            db = client[lista[1]]
            print("  > Database selecionada com sucesso")
        else:
            print("  > Esta database não existe")

    if command.startswith("add"):
        if db == '':
            print("   > Nenhuma database foi selecionada para isso")
        else:
            try:
                collection = db[lista[1]]
                for iten in lista[2::]:
                    splitado = iten.split(":")
                    key = splitado[0]
                    valor = splitado[1]
                    if valor[0]+valor[1] == "%i":
                        dicionario[key] = int(valor[2::])
                    elif valor[0]+valor[1] == "%f":
                        dicionario[key] = float(valor[2::])
                    elif valor[0]+valor[1] == "%s":
                        dicionario[key] = str(valor[2::])
                print(dicionario)
                collection.insert_one(dicionario)
            except:
                print("   > Um erro ocorreu tente novamente")

    if command.startswith("delete-one"):
        if db == '':
            print("   > Nenhuma database foi selecionada para isso")
        else:
            try:
                collection = db[lista[1]]
                for iten in lista[2::]:
                    splitado = iten.split(":")
                    key = splitado[0]
                    valor = splitado[1]
                    if valor[0]+valor[1] == "%i":
                        dicionario[key] = int(valor[2::])
                    elif valor[0]+valor[1] == "%f":
                        dicionario[key] = float(valor[2::])
                    elif valor[0]+valor[1] == "%s":
                        dicionario[key] = str(valor[2::])
                print(dicionario)
                collection.delete_one(dicionario)
                print(f"   > Item deletado com sucesso na coleção ( {collection.name} )")
            except:
                print("   > Um erro ocorreu tente novamente")
                    
    if command.startswith("find"):
        try:
            collection = db[lista[1]]
            for iten in lista[2::]:
                splitado = iten.split(":")
                key = splitado[0]
                valor = splitado[1]
                if valor[0]+valor[1] == "%i":
                    dicionario[key] = int(valor[2::])
                elif valor[0]+valor[1] == "%f":
                    dicionario[key] = float(valor[2::])
                elif valor[0]+valor[1] == "%s":
                    dicionario[key] = str(valor[2::])
            results = collection.find(dicionario)
            print("")
            print("     | DataBases")
            print("     ----------------------------------")
            print("")
            for result in results:
                print(f"         {result}")
            print("")
            print("     -----------------------------------")
            print("     |")
            print("")
        except:
            print("   > Um erro ocorreu tente novamente")

    if command.startswith("dump"):
        if db == '':
            print("  > Nenhuma database selecionada")
        else:
            if len(lista) == 1:
                search_data(db)
            if len(lista) >= 2:
                collection = db[lista[1]]
                search_data(collection)

    if command.startswith("show-databases"):
        results = client.list_database_names()
        print("")
        print("     | DataBases")
        print("     ----------------------------------")
        print("")
        for result in results:
            print(f"         {result}")
        print("")
        print("     -----------------------------------")
        print("     |")
        print("")

    if command.startswith("clear"):
        os.system('cls')
        inicio()

    if command.startswith("help"):
        if len(lista) < 2:
            print("""
    COMANDOS:

        HELP                -->  COMANDO DE AJUDA                            -->  HELP <command_name>
        SELECT-DB           -->  SELECIONAR A BASE DE DADOS                  -->  SELECT-DB <database_name>
        ADD                 -->  ADICIONAR ITEM EM UMA COLEÇÃO               -->  ADD  <collection_name> <key_1>:<value_1> <key_2>:<value_2>.....
        FIND                -->  PROCURA ITENS NA COLEÇÃO                    -->  FIND <collection_name> <key_1>:<value_1> <key_2>:<value_2>.....
        DUMP                -->  COMANDO PARA LISTAR COLLEÇÕES E ITENS       -->  DUMP or DUMP <collection_name>
        SHOW-DATABASES      -->  MOSTRA TODAS AS BASES DE DADOS              -->  SHOW-DATABASES
            """)
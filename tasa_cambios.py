import requests

apiKey = '6F93A481-A159-4B38-B143-0051FF10CA11'
moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()
     
while moneda_cripto != "" and moneda_cripto.isalpha():

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

    #print(r.status_code)#codigo 200 correcto que otro seria incorrecto

    #print(r.text)

    #ejercicio 1, como capturamos resultados correctos
    resultado = r.json() #guardamos el r.json en resultado(diccionario en python) 
    if r.status_code == 200:
        #ejercicio 3, como formateamos el valor rate en €
        print( "{:,.2f}€".format(resultado["rate"]) )

    #ejercicio 2, como capturamos errores
    else:
        print(resultado["error"])

    #ejercicio 4 como controlo input vacio, que no realize consulta si el input esta vacio
    moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()

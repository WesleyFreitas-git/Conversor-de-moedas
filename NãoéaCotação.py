# Refazer o cotação, do 0 e com defs
import requests
import matplotlib.pyplot as plt

dolar_grafico = []
euro_grafico = []
bitcoin_grafico = []

def dolar():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    a = request.json()

    global moeda1
    moeda1 = float(a["USDBRL"]["bid"])
    
    if moeda1 not in dolar_grafico:
        
        dolar_grafico.append(moeda1)

    print(f"\nO dólar está valendo, em real, aproximadamente: \nR$ {moeda1}")


def euro():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    a = request.json()

    global moeda2
    moeda2 = float(a["EURBRL"]["bid"])
    if moeda2 not in euro_grafico:
        
        euro_grafico.append(moeda2)

    print(f"\nO euro está valendo, em real, aproximadamente:\nR$ {moeda2}")
    

def bitcoin():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    a = request.json()

    global moeda3
    moeda3 = float(a["BTCBRL"]["bid"])
    if moeda3 not in bitcoin_grafico:
        
        bitcoin_grafico.append(moeda3)

    print(f"\nO bitcoin está valendo, em real, aproximadamente: \nR$ {moeda3}")


def grafico():
    x = ["Dólar", "Euro"]
    y = [moeda1,moeda2]

    plt.bar(x,y, color = 'blue')
    plt.title("Comparação")
    plt.xlabel("Moedas", color = 'blue')
    plt.ylabel("Valores", color = 'blue')
    plt.show()


def cotacao():
    while True:

        print("\n1. Dólar")
        print("2. Euro")
        print("3. Bitcoin")
        print("4. Sair")
        ask = input("\nEscolha uma das opções: " )

        if ask.lower() in ['1', "dolar", "dólar"]:
            dolar()
        elif ask.lower() in ['2', "euro"]:
            euro()
        elif ask.lower() in ["3", "bitcoin"]:
            bitcoin()
        elif ask.lower() in ["4", "sair"]:
            break
        else:
            print("Digite uma das opções.")


def interface():
    while True:
        print("Opções:")
        print("1. Ver cotação")
        print("2. Ver gráfico de comparação")
        ask = input("O que você deseja fazer? ")

        if ask.lower() in ['1', "cotação", "cotacao"]:
            cotacao()
        elif ask.lower() in ['2', "gráfico", "grafico"]:
            grafico()

interface()

# Refazer o cotação, do 0 e com defs
import requests
import matplotlib.pyplot as plt


def dolar():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    a = request.json()

    global moeda1
    moeda1 = float(a["USDBRL"]["bid"])
   
    print(f"\nO dólar está valendo, em real, aproximadamente: \n\033[92mR$ {moeda1:.2f}\033[0m")


def euro():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    b = request.json()

    global moeda2
    moeda2 = float(b["EURBRL"]["bid"])
   
    print(f"\nO euro está valendo, em real, aproximadamente:\n\033[92mR$ {moeda2:.2f}\033[0m")
    

def bitcoin():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    c = request.json()

    global moeda3
    moeda3 = float(c["BTCBRL"]["bid"])
   
    print(f"\nO bitcoin está valendo, em real, aproximadamente: \n\033[92mR$ {moeda3:.2f}\033[0m")


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
        print("""Opções:\n
1. Ver cotação
2. Ver gráfico de comparação\n""")
        
        ask = input("O que você deseja fazer? ")

        if ask.lower() in ['1', "cotação", "cotacao"]:
            cotacao()
            
        elif ask.lower() in ['2', "gráfico", "grafico"]:
            
            try:
                grafico()
            except:
                print("\n\033[91mValores insuficientes!!\033[0m\n")
        else:
            print("\nDigite uma das opções\n")
            
interface()

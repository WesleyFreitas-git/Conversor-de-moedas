import requests, graficos

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


def cotacao():
    while True:
        
        print('-' * 50)
        print("1. Dólar")
        print("2. Euro")
        print("3. Bitcoin")
        print("4. Sair")
   
        ask = input("\033[1;94mEscolha uma das opções: \033[0m" )

        if ask.lower() in ['1', "dolar", "dólar"]:
            dolar()
        elif ask.lower() in ['2', "euro"]:
            euro()
        elif ask.lower() in ["3", "bitcoin"]:
            bitcoin()
        elif ask.lower() in ["4", "sair"]:
            break
        else:
            print("\033[1;91mDigite uma das opções.\033[0m")


def interface():
    while True:
        print("""\n\033[1;94mOpções: 
1.\033[0m Ver cotação\033[1;94m
2.\033[0m Ver gráfico de comparação\033[0m""") 
        
        ask = input("\033[1;94mO que você deseja fazer? \033[0m")

        if ask.lower() in ['1', "cotação", "cotacao"]:
            cotacao()
            
        elif ask.lower() in ['2', "gráfico", "grafico"]:
            
            try:
                graficos.grafico_comparacao(moeda1, moeda2)
            except:
                print("\n\033[1;91mValores insuficientes!!\033[0m")
        else:
            print("\n\033[1;91mDigite uma das opções!!\n\033[0m")
            

interface()
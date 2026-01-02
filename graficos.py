import matplotlib.pyplot as plt

# Gráfico em barra para comparação

def grafico_comparacao(m1, m2):
    x = ["Dólar", "Euro"]
    y = [m1,m2]

    plt.bar(x, y, color = 'blue')
    plt.title("Comparação")
    plt.xlabel("Moedas", color = 'blue',)
    plt.ylabel("Valores", color = 'blue')
    plt.show()

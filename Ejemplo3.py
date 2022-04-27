import pandas as pd
import matplotlib.pyplot as plt
archive = pd.read_csv('WEO_Data.csv', thousands=',', decimal='.')
archive.rename(columns={'Country':'Pais'}, inplace=True)
archive.set_index('Pais', inplace=True)
años = list(map(str, range(2000, 2024)))

def graphic():
    peru = archive.loc['Peru', años]
    peru.plot(kind='bar')
    plt.title("Gráfica del PERÚ - PBI $")
    plt.ylabel('Billones de $')
    plt.xlabel('Años')
    plt.show()

def graphic_barras():
    peru = archive.loc['Peru', años]
    peru.plot(kind='barh')
    plt.title("Gráfica del PERÚ - PBI $")
    plt.xlabel('Billones de $')
    plt.show()

def grafico_barrash2():
    data=archive.sort_values(by='2022',ascending=True,inplace=True)
    data=archive['2022'].tail(10)
    data.plot(kind='barh')
    plt.title('Gráfica de 10 países')
    plt.xlabel('Millones de dólares')
    plt.show()


def grafico_area():
    archive.sort_values(by='2022', ascending = False, inplace = True)
    data = archive[años].head(5)
    data = data.transpose()
    data.plot(kind='area',alpha=0.35)
    plt.title('Gráfica de 5 países')
    plt.xlabel('Años')
    plt.ylabel('Top 5')
    plt.show()

graphic()

graphic_barras()

grafico_barrash2()

grafico_area()
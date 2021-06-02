
from bs4 import  BeautifulSoup
import requests
import pandas as pd

def zamora():

    url = 'https://www.marca.com/futbol/primera-division/zamora.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Jugadores - Equipo
    port = soup.find_all('th', class_='ue-table-trophies__th is-main')

    porteros = list()

    for i in port:
        porteros.append(i.text)

    #print(jugadores)

    #Coeficente goles
    coeGol = soup.find_all('td', class_='ue-table-trophies__td is-marked')

    coeGoles = list()

    for i in coeGol:
        coeGoles.append(i.text)

    #print(goles)


    #print(goles)
    df = pd.DataFrame({'Portero (equipo)': porteros, 'Coeficiente de goles recibidos': coeGoles})
    print(df)
    return df

#df.to_csv('Zamora30.csv')

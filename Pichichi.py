from bs4 import  BeautifulSoup
import requests
import pandas as pd

def pichichi():

    url = 'https://www.marca.com/futbol/primera-division/pichichi.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Jugadores - Equipo
    jug = soup.find_all('th', class_='ue-table-trophies__th is-main')

    jugadores = list()

    for i in jug:
        jugadores.append(i.text)

    #print(jugadores)

    #Goles totales
    gol = soup.find_all('td', class_='ue-table-trophies__td is-marked')

    goles = list()

    for i in gol:
        goles.append(i.text)

    #print(goles)


    #print(goles)
    df = pd.DataFrame({'Jugador (equipo)': jugadores, 'Goles': goles}, index=list(range(1,51)))
    print(df)
    return df
    #df.to_csv('Pichichi30.csv')
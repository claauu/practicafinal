import random
import numpy as np
import TopTwitter
import TopInstagram
import TopYouTube
import Pichichi
import Zamora
from bs4 import  BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

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
   
    return 1
    #df.to_csv('Pichichi30.csv')


def script_response(script):
    if script == "script_hora":
        return f"Son las {datetime.now().hour}:{datetime.now().minute}"

    if script == "script_numero_aleatorio":
        return str(random.randrange(100))


    if script == "script_busquedaTwitter" or script=="cuales son los perfiles mas seguidos en twitter":
        salto = ' '
        aux2 =  TopTwitter.twitter()
        for element in range (len(aux2["Nombre"])):
            salto += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'
        return f"Estas son las cuentas con mas seguidores en Twitter: <br> {salto}" 
    
    if script == "script_busquedaInstagram" or script=="cuales son los perfiles mas seguidos en instagram":
        salto1 = ' '
        aux2 =  TopInstagram.instagram()
        for element in range (len(aux2["Nombre"])):
            salto1 += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'        
        return f"Estas son las cuentas con mas seguidores en Instagram: <br> {salto1}"

    if script == "script_pichichi" or script=="quien es el pichichi":  
        df=pichichi()
        return f"Estos son los maximos goleadores: <br> {df}"  

    if script == "script_youtube" or script=="quienes son los mas seguidos en youtube": 
        salto3 = ' '
        aux2 =  TopYouTube.youtube()
        for element in range (len(aux2["Nombre"])):
            salto3 += f'<p>{aux2["Nombre"][element]} {aux2["Nombre del canal"][element]} {aux2["Seguidores"][element]}</p>'       
        return f"Estas son las cuentas mas seguidas en youtube: <br> {salto3}" 
    
    if script == "script_zamora" or script=="porteros menos goleados":      
        return f"Estos son los porteros menos goleados: <br> {Zamora.zamora()}" 
    
    if script=="hola":
        return f"Hola que quieres"
    
    else:
        return f"Lo siento no te he entendido nada"
    


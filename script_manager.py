import random
import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

def pichichi():

    # proxies = {"http": "http://10.10.1.10:3128/",
    #        "https": "http://10.10.1.10:1080"}

    
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


def twitter():
# trackanalytics 'Most Followed Twitter Profiles' url pagina
    url = 'https://www.trackalytics.com/the-most-followed-twitter-profiles/page/'

    user_list = []
    screen_name_list = []
    username_list = []
    # Itera por las paginas
    for num in range(1, 2):
        try:
            # Carga pagina
            query = url + str(num) + '/'
            response = urllib3.PoolManager().request('GET', query).data

            # Evita warnings de decoding 
            FromRaw = lambda r: r if isinstance(r, str) else r.decode('utf-8', 'ignore')

            # Parsea html de la pag
            soup = BeautifulSoup(FromRaw(response), 'html.parser')

            # Extrae los elementos de la fila en la tabla de usuarios 
            rows = soup.find_all('tr')[1:16]
            for row in rows:
                try:
                    # Parsea las filas para extraer el link con el usuario de twitter
                    new = BeautifulSoup(str(row), 'html.parser').find_all('a')[1]
                    new2 = BeautifulSoup(str(row), 'html.parser').find_all('td')[2]
                    screen_name = new.get('title')
                    username = "@" + new.get('href').split('/')[-2]  # coge usuario por link
                
                    followers = str(new2).split('\n')
                    followers = followers[1].strip()
                    followers = followers.split(' ')
                    followers = followers[0]
                
                    # Almacena usuarios en user_list
                    user_list.append({'Nombre': screen_name, 'Usuario': username, 'Seguidores': followers})

                except Exception as e:
                    print('link error:', num, e)
                    continue
        except Exception as e:
            print('page error:', num, e)
            continue    

    df = pd.DataFrame(user_list)
    print(df)
    return df
#df.to_csv('MasSeguidosTwitter19.csv')

# %%

def instagram():
    url = 'https://www.trackalytics.com/the-most-followed-instagram-profiles/page/'

    # list of [screen name, username] for each popular page
    user_list = []
    screen_name_list = []
    username_list = []
    # Itera por las paginas
    for num in range(1, 2):
        try:
             # Carga pagina
            query = url + str(num) + '/'
            response = urllib3.PoolManager().request('GET', query).data

            # Evita warnings de decoding 
            FromRaw = lambda r: r if isinstance(r, str) else r.decode('utf-8', 'ignore')

            # Parsea html de la pag
            soup = BeautifulSoup(FromRaw(response), 'html.parser')

            # Extrae los elementos de la fila en la tabla de usuarios 
            rows = soup.find_all('tr')[1:16]
            for row in rows:
                try:
                   # Parsea las filas para extraer el link con el usuario de twitter
                    new = BeautifulSoup(str(row), 'html.parser').find_all('a')[1]
                    new2 = BeautifulSoup(str(row), 'html.parser').find_all('td')[2]
                    screen_name = new.get('title')
                    username = "@" + new.get('href').split('/')[-2]  # coge usuario por link
                    
                    followers = str(new2).split('\n')
                    followers = followers[1].strip()
                    followers = followers.split(' ')
                    followers = followers[0]
                    # Almacena usuarios en user_list
                    user_list.append({'Nombre': screen_name, 'Usuario': username, 'Seguidores': followers})

                except Exception as e:
                    print('link error:', num, e)
                    continue
        except Exception as e:
            print('page error:', num, e)
            continue

            # print(user_list)

    df = pd.DataFrame(user_list)
    print(df)
    return df
#df.to_csv('MasSeguidosInsta20.csv')

def youtube():

    url = 'https://www.trackalytics.com/the-most-subscribed-youtube-users/page/'

    # list of [screen name, username] for each popular page
    user_list = []
    screen_name_list = []
    username_list = []
    # Iterate through site pages
    for num in range(1, 2):
        try:
            # Load page
            query = url + str(num) + '/'
            response = urllib3.PoolManager().request('GET', query).data

            # Avoid decoding warnings
            FromRaw = lambda r: r if isinstance(r, str) else r.decode('utf-8', 'ignore')

            # Parse page html
            soup = BeautifulSoup(FromRaw(response), 'html.parser')

            # Extract row elements in table of users
            rows = soup.find_all('tr')[1:16]
            for row in rows:
                try:
                    # Parse row to extract link with twitter user
                    new = BeautifulSoup(str(row), 'html.parser').find_all('a')[1]
                    new2 = BeautifulSoup(str(row), 'html.parser').find_all('td')[2]
                    screen_name = new.get('title')
                    username = new.get('href').split('/')[-2]  # get username from link
                    # print(new2.prettify())
                    followers = str(new2).split('\n')
                    followers = followers[1].strip()
                    followers = followers.split(' ')
                    followers = followers[0]
                    # print(followers)
                    # Store user in user_list
                    user_list.append({'Nombre': screen_name, 'Nombre del canal': username, 'Seguidores': followers})

                except Exception as e:
                    print('link error:', num, e)
                    continue
        except Exception as e:
            print('page error:', num, e)
            continue

            # print(user_list)

    df = pd.DataFrame(user_list)
    print(df)
    return df

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

def script_response(script):
    if script == "script_hora" or script== "que hora es":
        return f"Son las {datetime.now().hour}:{datetime.now().minute}"

    if script == "script_numero_aleatorio" or script== "dime un numero aleatorio":
        return str(random.randrange(100))


    if script == "script_busquedaTwitter" or script=="cuales son los perfiles mas seguidos en twitter":
        salto = ' '
        aux2 = twitter()
        for element in range (len(aux2["Nombre"])):
            salto += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'
        return f"Estas son las cuentas con mas seguidores en Twitter: <br> {salto}" 
    
    if script == "script_busquedaInstagram" or script=="cuales son los perfiles mas seguidos en instagram":
        salto1 = ' '
        aux2 = instagram()
        for element in range (len(aux2["Nombre"])):
            salto1 += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'        
        return f"Estas son las cuentas con mas seguidores en Instagram: <br> {salto1}"

    if script == "script_pichichi" or script=="quien es el pichichi":  
        return f"Estos son los maximos goleadores: <br> {pichichi()}"  

    if script == "script_youtube" or script=="quienes son los mas seguidos en youtube": 
        salto3 = ' '
        aux2 = youtube()
        for element in range (len(aux2["Nombre"])):
            salto3 += f'<p>{aux2["Nombre"][element]} {aux2["Nombre del canal"][element]} {aux2["Seguidores"][element]}</p>'       
        return f"Estas son las cuentas mas seguidas en youtube: <br> {salto3}" 
    
    if script == "script_zamora" or script=="porteros menos goleados":      
        return f"Estos son los porteros menos goleados: <br> {zamora()}" 
    
    if script=="hola":
        return f"Hola que quieres"
    
    else:
        return f"Lo siento no te he entendido nada"
    


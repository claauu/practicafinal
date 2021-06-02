from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
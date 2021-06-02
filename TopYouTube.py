from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    #df.to_csv('MasSeguidosYoutube20.csv')
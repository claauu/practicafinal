import random
import numpy as np
import TopTwitter
import TopInstagram
import TopYouTube
import Pichichi
import Zamora
from datetime import datetime


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
        return f"Estos son los maximos goleadores: <br> {Pichichi.pichichi()}"  

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
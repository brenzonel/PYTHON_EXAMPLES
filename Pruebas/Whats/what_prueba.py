import pywhatkit
import os
from dotenv import load_dotenv

load_dotenv(override=True) #Carga de variables de ambiente con override si existe un archivo env
numero = os.getenv('NUMERO') #Numero en variables de ambiente
group = os.getenv('GROUP_NAME') #Nombre de grupo en variables de ambiente

phone_numer = numero #'+5211111111'
group_id = group
message = 'Mensaje a enviar' 
time_hour = 20
time_minute = 3
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 5
mode = "contact"    # "contact" or "group"

try:
    if mode == "contact":
        pywhatkit.sendwhatmsg(phone_numer, 
                              message, 
                              time_hour, 
                              time_minute, 
                              waiting_time_to_send, 
                              close_tab, 
                              waiting_time_to_close)
    elif mode == "group":
        pywhatkit.sendwhatmsg_to_group(group_id, 
                                       message, 
                                       time_hour, 
                                       time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)

except Exception as e:
    print(f'An error ocurred: {e}')
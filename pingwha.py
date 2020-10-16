from colorama import Back, Fore, init, Style
#from win10toast import ToastNotifier
import pyfiglet
import time
import datetime
import random
import os
import csv
import re
import subprocess
from twilio.rest import Client




print()
clean_window='clear'
os.system(clean_window)
print(Fore.WHITE+Style.BRIGHT+"Web Site          -          www.davenisc.com")
print(Fore.WHITE+"     __      "+Fore.GREEN+"  ______ _             _    _ _           ")
print(Fore.YELLOW+"  -="+Fore.WHITE+"("+Fore.GREEN+"o"+Fore.WHITE+" '.   " +Fore.GREEN+"   | ___ (_)           | |  | | |          ")
print(Fore.WHITE+"     '.-.\   "+Fore.GREEN+"  | |_/ /_ _ __   __ _| |  | | |__   __ _ ")
print(Fore.WHITE+"      /|  \\  "+Fore.GREEN+"  |  __/| | '_ \ / _` | |/\| | '_ \ / _` |")
print(Fore.WHITE+"      '|  ||  "+Fore.GREEN+" | |   | | | | | (_| \  /\  / | | | (_| |")
print(Fore.YELLOW+"       _"+Fore.WHITE+"\_):"+Fore.YELLOW+",_"+Fore.GREEN+" \_|   |_|_| |_|\__, |\/  \/|_| |_|\__,_|")
print(Fore.GREEN+"                               __/ |               ")
print(Fore.GREEN+"                              |___/             ")
print(Fore.CYAN+Style.BRIGHT+"   Version:"+Fore.RED+" 1"+Fore.WHITE+"."+Fore.RED+"0")
print(Fore.CYAN+Style.BRIGHT+"   compatible: "+Fore.RED+"Linux "+Fore.WHITE+"all versions")
print(Fore.CYAN+Style.BRIGHT+"   Twitter: "+Fore.RED+"@"+Fore.WHITE+"davenisc")
print()


# ---------------------- disclaimer -----------------

print(Fore.RED+"NOTE:"+Fore.YELLOW+"This tool works with Twilio for its perfect ")
print(Fore.YELLOW+"operation, please register and create your tokens ")
print(Fore.YELLOW+"before using it.")
print(Fore.WHITE+"")


# --------------------- IP a monitorear --------------

ip_monitor = input("Please enter IP to monitor : ")
hostname_monitor = input("Please enter a name or hostname for the IP to monitor : ")
numero_whatsapp = input("Please enter your registered WhatsApp number: ")
print()


#-------------------------------guardar datos en archivo
archivo = open("csv_monitor.csv","w")
archivo.write(str((f'{hostname_monitor},{ip_monitor}''\n')))
archivo.close()

# --------------------

def check_ping(hostname):

    response = os.system("ping -c 1 " + hostname + "> log-ping-perz.txt" )
    count_response = os.system('grep "received" log-ping-perz.txt > log-respuesta-ping.txt' )
    count_lines_response = os.system('cat log-respuesta-ping.txt | wc -l > num-log-respuesta-ping.txt' )
    data_graph_1 = os.popen('cat num-log-respuesta-ping.txt').read()


    #-------------------------------guardar datos en archivo


    # --------------------

    if response == 0:
        response = os.system("clear" )
        print()
        print(Fore.GREEN+Style.BRIGHT+"Web site          -          www.davenisc.com")
        ascii_banner = pyfiglet.figlet_format("Diagnosis")
        print(Fore.WHITE+ascii_banner)
        print(Fore.GREEN+Style.BRIGHT+f"  Running monitoring -  {hostname_monitor} flawless")
        print()
        check_ping = "[OK]"



    else:
        response = os.system("clear" )
        print()
        print(Fore.RED+Style.BRIGHT+"Web site          -          www.davenisc.com")
        ascii_banner = pyfiglet.figlet_format("Diagnosis")
        print(Fore.WHITE+ascii_banner)
        print(Fore.RED+Style.BRIGHT+f"  Running monitoring -  {hostname_monitor} fallen")
        print()
        check_ping = "[Error]"

    return check_ping

# Lee los datos del archivo y los guarda en una variable.
archivo_servidores = open('csv_monitor.csv')
servidores_reader = csv.reader(archivo_servidores)
datos_servidores = list(servidores_reader)

# Prueba si hay conexión en todos los servidores
contador = 0

while True:
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_ping(datos_servidores[i][1])

        if resultado == "[Error]":
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.RED + resultado))
                # ------------ mensajes en pantalla
            print()
            print(Fore.WHITE+"Latency = "+Fore.RED+" Timeout")
            print()
            print(Fore.YELLOW+"To stop monitoring press Control + C ")


            # --------------  codigo para envio de mensajes WhatsApp
            account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                          from_='whatsapp:+xxxxxxxxxxx',
                                          body=f'Alert! {hostname_monitor} is down.',
                                          to=f'whatsapp:+57{numero_whatsapp}'
                                      )
            print()
            print(Fore.WHITE+"Message "+Fore.GREEN+"WhatsApp "+Fore.WHITE+"sent!")
            print()
            print("Twilio validation code: ",message.sid)
            print()
        else:
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.GREEN + resultado))
            print()
            latency_data = os.system("grep 'time=' log-ping-perz.txt > time-log.txt | awk '{ print $7 }' time-log.txt > latency-time.txt")
            latency_final = os.popen('cat latency-time.txt').read()
            print(Fore.WHITE+"Latency "+Fore.RED+"►"+Fore.GREEN,latency_final)
    contador += 1

    print()

    # Pausa de 1 minutos.
    time.sleep(1)

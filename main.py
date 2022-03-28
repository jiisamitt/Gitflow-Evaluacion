from hashtag import hash
from dias import dias
from retweet import retweet
from usuarios import usuarios
from time import sleep
print("Presione 1 para obtener los 10 dias  con más tweets")
print("Presione 2 para obtener los 10 retweeted con más tweets")
print("Presione 3 para los 10 usuarios con más tweets")
print("Presione 4 para los 10 hashtags con más tweets")
user_choice = input("Indique su número aquí:")

if user_choice == "1":
    print("Esto puede demorar un poco")
    dias()
    print("Ya están los resultados, tiene 20 segundos para revisarlos, luego se cerrará el programa")
elif user_choice == "2":
    print("Esto puede demorar un poco")
    retweet()
    print("Ya están los resultados, tiene 20 segundos para revisarlos, luego se cerrará el programa")
elif user_choice == "3":
    print("Esto puede demorar un poco")
    usuarios()
    print("Ya están los resultados, tiene 20 segundos para revisarlos, luego se cerrará el programa")
elif user_choice == "4":
    print("Esto puede demorar un poco")
    hash()
    print("Ya están los resultados, tiene 20 segundos para revisarlos, luego se cerrará el programa")
else:
    print("No seleccionaste ninguna opción correcta, vuelve a intentarlo")
    exit()
sleep(20)
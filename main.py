import selenium
from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title YOUTUBE VIEWBOT')

print(pyfiglet.figlet_format("BOT YOUTUBE ELIE", font="slant"))
print("!VOUS DEVREZ ACCEPTER LES COOKIES LA PREMIERE FOIS ET LANCER LA VIDEO!")
vidUrl = input("Lien de la video: ")
tps = int(input("Combien de temps les bots doivent ils rester sur la video (conseiller : 20s) : "))
nb = int(input("Combien de vues souhaitez vous : "))

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome( options=chrome_options)
driver.set_window_size(500,500)
i=1
for i in range(nb):
        driver.get(vidUrl)
        sleep(tps)
        driver.refresh()
        print("Nombre de vues ajoutees : ",i)
driver.close()
print("ajout de vues terminer.")
print("Appuyer sur entrer pour quitter")
input()
exit()
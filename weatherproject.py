#!/usr/bin/env python3



# This software use wttr.in, look at https://wttr.in/:help for more information about it.
# you need the easygui and wget library for Python 3.


import wget
from easygui import *  # sudo pip3 install pillow if needed and easygui
import unidecode  # sudo pip3 install unidecode
import os
import logging

# Weather result

# class creation
class Weather:
    def __init__(self):
        self.city = "Bern"
        self.unnaccent_city = "Bern"
        self.lng = "German"
        self.url = "http://wttr.in/"
        self.filePath = ""
        self.image = "meteo.png"

#create log file to show errors and inputs
logging.basicConfig(
    filename="weather.log",
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def weather():
    if Weather.city == None:  # if nothing the default city is Bern
        Weather.city = "Bern"
    elif Weather.city == "":
        Weather.city = "Bern"
    Weather.unaccent_city = unidecode.unidecode(
        Weather.city
    )  # remove accent and all non-ascii characters
    logging.info(Weather.city)
    Weather.url = (
        ("http://wttr.in/")
        + str(Weather.unaccent_city)
        + str("_Fp_lang=")
        + str(Weather.lng)
        + str(".png")
    )
    try:
        filename = wget.download(Weather.url, out="meteo.png")
        logging.info("Server online OK")
    except:
        logging.critical("No answer from the server")   #add failures to the log file
    logging.info(filename)
    Weather.image = "meteo.png"
    msg = "This is the weather report for this location"
    choices = ["Change city"]
    reply = buttonbox(msg, image=Weather.image, choices=choices)
    if reply == "Change city":
        location()


# Location selection


def location():
    Weather.filePath = "meteo.png"

    if os.path.exists(Weather.filePath):
        os.remove(Weather.filePath)
    else:
        print("")
    msg = "Enter a city or a location\n\nBy defautl it's Bern - Switzerland"
    title = "Location"
    default = "Bern"
    Weather.city = enterbox(msg, title, default)
    if Weather.city == None:  # if nothing the default city is Bern
        Weather.city == "Bern"
    elif Weather.city == "":
        Weather.city = "Bern"
    weather()


# Language selection
def language():
    msg = "What is your language ?"
    title = "Languages"
    choices = [
        "English",
        "German",
        "French",
        "Danish",
        "Persian",
        "Indonesian",
        "Italian",
        "Norwegian Bokmål",
        "Dutch",
        "Russian",
        "Afrikaans",
    ]
    choice = choicebox(msg, title, choices)

    if choice == "Afrikaans":
        Weather.lng = "af"
    elif choice == "Danish":
        Weather.lng = "da"
    elif choice == "German":
        Weather.lng = "de"
    elif choice == "French":
        Weather.lng = "fr"
    elif choice == "Persian":
        Weather.lng = "fa"
    elif choice == "Indonesian":
        Weather.lng = "id"
    elif choice == "Italian":
        Weather.lng = "it"
    elif choice == "Norwegian Bokmål":
        Weather.lng = "nb"
    elif choice == "Dutch":
        Weather.lng = "nl"
    elif choice == "Russian":
        Weather.lng = "ru"
    elif choice == None:  # if nothing it's english
        Weather.lng = "en"
    else:
        Weather.lng = "en"  # Default is english

    location()


language()

import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
from googlesearch import search
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<17:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname =("Jarvis")
    speak("I am your Assistant"+assname)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("How can i Help you"+uname)
 
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        return "None"
    return query




if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    usrname()
    while True:
        query = takeCommand().lower()

        if query==0:
            continue
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'open youtube' in query:
            speak("what do u want to play on youtube sir")
            stat = takeCommand()
            url='https://youtube.com/search?q='+stat
            webbrowser.get().open(url)

        elif 'search google' in query:
            speak("what do you want to search on google sir")
            stat = takeCommand()
            url='https://www.google.com/search?q='+stat
            webbrowser.get().open(url)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")


        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("going down enjoy your day sir")
            exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who are you" in query:
            speak("I am your virtual assistant created by Shivraj")

        elif "don't listen" in query or "stop" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print("sleeping time"+a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "go to sleep" in query or "sleep" in query:
            speak("going on sleep mode")
            subprocess.call(["shutdown", "/h"])

        elif "log off" in query or "shutdown" in query:
            speak("Make sure all the application are closed before shutdown")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        
        elif "are you there" in query:
            wishMe()
            speak("always in your service sir")
            speak(assname)

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            city_name = takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature (in kelvin unit)" +str(current_temperature)+"\n atmospheric pressure (in hPa unit)"+str(current_pressure) +"\n humidity (in percentage)" +str(current_humidiy) +"\n description" +str(weather_description))

            else:
                speak("City Not Found")

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")


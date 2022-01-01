from main import *
import wolframalpha
import speech_recognition as sr # recognise speech
import face_recognition as fr
import face_recognition
import numpy as np
from time import sleep
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from datetime import datetime # get time details
import webbrowser # open browser
import ssl
import wikipedia
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import json
import datetime
import psutil
import screen_brightness_control as sbc
import cv2
from googletrans import Translator
import pyjokes
import warnings
#import PyPDF2



if (success == "False"):
    engine_speak("Unauthorised person")
    time.sleep(2)
    exit()


class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

'''
def alarm():
    import datetime
    from playsound import playsound
    now = datetime.datetime.now()
    current_hour = now.hour
    current_min = now.minute
    if current_hour == 6 and current_min == 40:
       playsound('C:\\Users\\SHIVRAJ\\Desktop\\Jarvis\\jarvis_alarm.wav')
'''
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        engine_speak("Good Morning sir, How may i help u")
    elif hour>=12 and hour<17:
        engine_speak("Good Afternoon sir, How may i help u")
    else:
        engine_speak("Good Evening sir, How may i help u")

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def wifiinfo():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])#meta data of wifi network
    data = meta_data.decode('utf-8', errors ="backslashreplace")#decoding meta data from byte to string
    data = data.split('\n')#splitting data string to list
    names = []#list for wifi names
    for i in data:
        if "All User Profile" in i :
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            names.append(i)
    return names[-1]

def brightness():
    current_brightness = sbc.get_brightness()
    return current_brightness

def work():
    im = Image.open("friday.png")
    im.show()

def get_encoded_faces():
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

def unknown_image_encoded(img):
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

def classify_face(im):
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
        cv2.imshow('Face Recognition', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return face_names
'''
def detectperson():
    engine_speak("detecting sir")
    classify_face("Test/test.jpg")
    engine_speak("detected")
'''
def telltime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    engine_speak(current_time)


r = sr.Recognizer() # initialise a recogniser

def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text..
        except sr.UnknownValueError: # error: recognizer does not understand..
            time.sleep(0.01)
        except sr.RequestError:
            engine_speak('Sorry cannot hear you') # error: recognizer is not connected..
        print(voice_data.lower()) # print what user said
        #clear = lambda: os.system('cls')
        #clear()
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3..
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file..

def tellweather():
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = record_audio("city name")
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        engine_speak("Temperature (in kelvin unit)" +str(current_temperature)+"\n humidity (in percentage)" +str(current_humidiy))
    else:
        engine_speak("City Not Found")

def googlesearch():
    search_term = record_audio("what do u want to search on google sir")
    url = "https://www.google.com/search?q="+search_term
    webbrowser.get().open(url)
    engine_speak("here what i found for " + search_term + " on google")

def openyoutube():
    search_term = record_audio("what do u want to search on youtube sir")
    url = "https://www.youtube.com/search?q="+search_term
    webbrowser.get().open(url)
    engine_speak("here what i found for " + search_term + " on youtube")

def maps():
    url = "https://www.google.com/maps/search/Where+am+I+?/"
    webbrowser.get().open(url)
    engine_speak("You must be somewhere near here sir, as per Google maps")

def facebook():
    engine_speak("connecting to facebook sir")
    url = "https://www.facebook.com"
    webbrowser.get().open(url)

def instagram():
    engine_speak("Connecting to instagram, enjoy latest reels sir")
    url = "https://www.instagram.com"
    webbrowser.get().open(url)

def spotify():
    engine_speak("Connecting to spotify")
    url = "https://open.spotify.com/playlist/6N4R1O2AuBYJVjUksEKTgN"
    webbrowser.get().open(url)

def hotstar():
    engine_speak("opening hotstar")
    url = "https://www.hotstar.com/in"
    webbrowser.get().open(url)

def openwhatsapp():
    engine_speak("Connecting to whatsapp")
    url = "https://web.whatsapp.com/"
    webbrowser.get().open(url)

def news():
    engine_speak("Here are some headlines from Times of India sir")
    url = "https://timesofindia.indiatimes.com/home/headlines"
    webbrowser.get().open(url)

def classroom():
    engine_speak("Opening classroom")
    url = "https://classroom.google.com/u/2/h"
    webbrowser.get().open(url)

def searchplace():
    place = record_audio("which place u want to search")
    url= "https://www.google.com/maps/search/" + place
    webbrowser.get().open(url)

def imagecapture():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while result:
        ret, img = cap.read()
        r = random.randint(1,1000)
        path = "C:\\Users\\SHIVRAJ\\Desktop\\Jarvis\\pictures\\"+str(r)
        cv2.imwrite(path+'.jpg', img)
        result = False
    cap.release()
    cv2.destroyAllWindows()

def videocapture():
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    r = random.randint(1,1000)
    path = "C:\\Users\\SHIVRAJ\\Desktop\\Jarvis\\videos\\"+str(r)
    result = cv2.VideoWriter(path+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)
    while(True):
        ret, frame = video.read()
        if ret == True: 
            result.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(40) == 27:
                break
        else:
            break
    video.release()
    result.release()
    cv2.destroyAllWindows()
'''
def audiobook():
    path = open('C:\\Users\\SHIVRAJ\\Desktop\\Jarvis\\audiobooks\\edward.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    from_page = pdfReader.getPage(7)
    text = from_page.extractText()
    engine_speak(text)

def todolist():
    todolist = []
    listtitle = record_audio("what do u want to call the list sir")
    todolist.append(listtitle)
    tasks = []
    while(True):
        i = record_audio("tell me the task")
        if(i == "finish"):
           engine_speak("to do list created")
           break
        if(i != ""):
           tasks.append(i)
        print(tasks)
'''
def respond(voice_data):
    '''
    # 1: detect faces 
    if there_exists(["detect person"]):
        detectperson()
    '''
    # 2: name(assistant)
    if there_exists(["who are you"]):
        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name} i am your virtual assistant")

    # 3: calculator
    if there_exists(["open calculator"]):
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    # 4: notepad
    if there_exists(["open notepad"]):
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    # 5: name(person)
    if there_exists(["tell me my name"]):
        engine_speak("Your name must be " + person_obj.name)

    # 6: test of friday's speed
    if there_exists(["are you there"]):
        engine_speak("always in your service sir")
    '''
    # 7: greeting(assistant)
    if there_exists(["how are you"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
    '''
    # 8: time
    if there_exists(["tell me the time"]):
        telltime()

    #9: weather
    if there_exists(["tell me weather status"]):
        tellweather()

    #10: google something
    if there_exists(["search google"]):
        googlesearch()

    #11: search something on youtube
    if there_exists(["open youtube"]):
        openyoutube()
    '''
    #12: open command prompt
    if there_exists(["cmd"]):
        os.system("start cmd")
    '''
    # 13: exit
    if there_exists(["exit"]):
        engine_speak("enjoy your day sir,bye")
        exit()
   
    # 14: Current location as per Google maps
    if there_exists(["track my location"]):
        maps()

    #15: Facebbok
    if there_exists(["open facebook"]):
        facebook()

    #16: Instagram
    if there_exists(["want some fun"]):
        instagram()

    #17: Spotify
    if there_exists(["play music"]):
        spotify()

    #18: hotstar
    if there_exists(["open hotstar"]):
        hotstar()

    #19: whatsapp
    if there_exists(["open whatsapp"]):
        openwhatsapp()

    #20: news
    if there_exists(["tell me the news"]):
        news()

    #21: classroom
    if there_exists(["open classroom"]):
        classroom()

    #22: search place on map
    if there_exists(["search place"]):
        searchplace()

    #23: inbox
    if there_exists(["open gmail"]):
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
 
    #24: system report
    if there_exists(["system report"]):
       battery = psutil.sensors_battery()
       engine_speak("Battery percentage is " + str(battery.percent))
       #engine_speak(battery.percent)
       if battery.power_plugged:
          engine_speak("System is in charging mode")
       else:
          engine_speak("System is not in charging mode")
       engine_speak("Current wifi that system has connected to is " + wifiinfo())
       engine_speak("Brightness of the system is " + str(brightness()))

    #25: what can u do
    if there_exists(["what can you do"]):
        engine_speak("I can google,open websites,search place on map, for all commands i'm opening commands chart sir")
        work()
    '''
    #26: detect object
    if there_exists(["detect this"]):
        engine_speak("detecting sir")
        import OD
        engine_speak("objects detected")
        clear = lambda: os.system('cls')
        clear()
    '''

    #27: tell me a joke
    if there_exists(["tell me a joke"]):
       engine_speak("searching a joke")
       My_joke = pyjokes.get_joke(language="en", category="all")
       engine_speak(My_joke)
       order2 = record_audio("sir ,do u want to listen more jokes?")
       if(order2 == "yes"):
          engine_speak("let me tell u another joke")
          joke3 = pyjokes.get_joke(language="en", category="all")
          engine_speak(joke3)

    #28: open camera
    if there_exists(["open camera"]):
       order = record_audio("sir do u want to capture a image or video")
       if(order == "image" or order == "images"):
          imagecapture()
       else:
          videocapture()
    '''
    #29: play audiobook
    if there_exists(["audiobook"]):
        audiobook()
    '''
    '''
    #31: make a to do list
    if there_exists(["create a list"]):
        todolist()
    '''

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Friday'
person_obj.name = "Shiv"
wishMe()
engine = pyttsx3.init()

commands = ["","who are you","open calculator","open notepad","tell me my name","are you there","tell me the time","tell me weather status","search google","open youtube","exit","track my location","open facebook","want some fun","play music","open hotstar","open whatsapp","tell me the news","open classroom","search place","open gmail","system report","what can you do","tell me a joke","open camera"]

newvoice_data = []

while(1):
    #alarm()
    voice_data = record_audio("") # get the voice input

    if(voice_data not in commands):
       #from nltk.tokenize import sent_tokenize
       import wikipediaapi as wa
       import nltk
       from nltk.stem import WordNetLemmatizer
       from nltk.corpus import stopwords

       language = "en"
       testdata = wa.Wikipedia(language)
       #newvoice_data = sent_tokenize(voice_data)
       lemmatizer = WordNetLemmatizer()
       words = nltk.word_tokenize(voice_data)
       words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
       newvoice_data = ' '.join(words)
       print(newvoice_data)
       if(testdata.page(newvoice_data).exists):
          try:
              engine_speak("connecting to oracle")
              page = wikipedia.summary(newvoice_data, sentences=2)
              engine_speak(page)
          except wikipedia.exceptions.PageError:
              continue
          except wikipedia.DisambiguationError as e:
              s = random.choice(e.options)
              engine_speak(s)
    if(voice_data != ""):
       respond(voice_data) # respond

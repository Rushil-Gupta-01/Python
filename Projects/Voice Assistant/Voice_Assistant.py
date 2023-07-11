import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser 
from googlesearch import search

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Listening.....')
        recordedaudio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(recordedaudio,language='en_US')
        command=command.lower()
        print('Your message:',format(command))

    except Exception as ex:
        print(ex)
    if 'search for' in command:
        query = command.replace('search for','')
        a='Searching for ' + query + '...'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        for x in search(query,2):
            print(x)
        subprocess.Popen([programName])

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    
    
    if 'play' in command:
        song = command.replace('play','')
        a='Playing ' + song
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(command)


    if 'youtube' in command:
        b='Opening Youtube....'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/')

    if 'whatsapp' in command:
        x = 'Opening Whatsapp....'
        engine.say(x)
        engine.runAndWait()
        programmeName = 'C:\\Users\\india\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
        subprocess.Popen([programmeName])

    if 'github' in command:
        b='Opening Github....'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://github.com/RushilGupta01/Python')

    if 'udemy' in command:
        b='Opening Udemy....'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478294#content')

    if 'weather' in command:
        b="Today's weather...."
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.bing.com/search?q=wether&cvid=2572a78cef0d4d5d9db3dd0beebe6760&aqs=edge..69i57j0l5j69i60l3.2381j0j1&pglt=641&FORM=ANNTA1&PC=U531')



while True:
    cmd()

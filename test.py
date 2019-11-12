import speech_recognition as sr
import webbrowser
import os
import sys
# get audio from the microphone
r = sr.Recognizer()

def assistant(command):


    if 'Notepad' in command:
       os.system("notepad")

    elif 'shutdown' in command:
        SpeakText('Bye  Bro. Have a nice day')
        print("Bye  Bro. Have a nice day")
        try:
         os._exit(0)
        except:
         print("done")


    elif 'open' in command:
        #reg_ex = re.search('open (.+)', command)
        #if reg_ex:
        #   domain = reg_ex.group(1)
        #    print(domain)
        url = 'https://www.' + command
        webbrowser.open(url)

    elif 'chrome' in command:
        url = 'https://www.' + command
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'notepad' in command:
        os.system("notepad")


def StartListening(ted):

 try:


    re="You said " + r.recognize_google(ted)
    if 'listen' in re:
     print("Listening Buddy")
     SpeakText("Listening Buddy")
     #SpeakText(re)
     with sr.Microphone() as source:
       r.adjust_for_ambient_noise(source, duration=0.5)
       audio2 = r.listen(source)
     StartListening(audio2)
     SpeakText(r.recognize_google(audio2))
     assistant(r.recognize_google(audio2))
     startListen()

 except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
 except sr.UnknownValueError:
     print("",end="")









import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
def SpeakText(command):
    speak.Speak(command)


def startListen():
 while(1):
  with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source, duration=0.5)
     #print("Speak:")
     audio = r.listen(source)
     StartListening(audio)

startListen()

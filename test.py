import speech_recognition as sr  
import webbrowser
import os
import sys
import datetime
import smtplib
import subprocess
# get audio from the microphone                                                                       
r = sr.Recognizer()     
file=1
s="Sleep"
def SpeechToText():   
    audio2 = r.listen(source2)
    MyText=r.recognize_google(audio2)
    MyText=MyText.lower()
    #if(s!="Sleep"):
    return MyText
    
    

def assistant(command):
    

    if 'notepad' in command:
       os.system("notepad")
       return   
    elif 'time' in command:
         time=datetime.datetime.now()
         t="the time is "+str(time.hour)+" hours "+str(time.minute)+" minutes"
         SpeakText(t)
         print(t)
    
    elif 'shutdown' in command:
        SpeakText('Bye  Bro. Have a nice day')
        print("Bye  Bro. Have a nice day")
        try:
         os._exit(0)
        except:
         print("done")
    elif 'launch' in command:
        command=command.lstrip('launch')
        SpeakText('Launching '+command)
        print('Launching '+command)
        try:
         os.system("command")
         #subprocess.Popen(['C:\ProgramFiles\MozillaFirefox\chrome.exe'])
        except:
         print("done")    
   
    elif 'open' in command:
        
        url = 'https://www.' + command
        webbrowser.open(url)
        return

    elif 'search' in command:
        command=command.lstrip('search')
        command=command.lstrip('Search')
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "https://www.google.com.tr/search?q={}".format(command)
        webbrowser.get(chrome_path).open(url)
        return       
    elif 'chrome' in command:
        url = 'https://www.' + command
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        return
    elif 'email' in command:
            SpeakText('Who is the recipient?')
            recipient = SpeechToText()
        
            SpeakText('What should I say to him?')
            content = SpeechToText()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('hameedkunkanoor@gmail.com', 'pwd123')
            mail.sendmail('sender_email', 'recipient', content)
            mail.close()
            SpeakText('Email has been sent successfuly. You can check your inbox.')

           
    elif 'notes' in command:
        SpeakText("Noting down sir")
        text=SpeechToText() 
        global file
        myfile="Mynotes"+str(file)+".txt"
        file+=1
        f= open(myfile,"w+")
        f.write(text)
        f.close() 
        SpeakText("saved your notes with name"+myfile)
        return
    
    return



    
 








import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
def SpeakText(command):
    speak.Speak(command)
    print(command)

with sr.Microphone() as source2:
 while(1):
    
     try:
          
          
           
           r.adjust_for_ambient_noise(source2, duration=0.1)
           audio2 = r.listen(source2)
           MyText=r.recognize_google(audio2)
           MyText=MyText.lower()
           #if(s!="Sleep"):
           if(s=="Active"):
               
               
               assistant(MyText)
           elif(s=="Sleep"):
              
               if 'awake' or 'awake' or 'listen' or 'hey' or 'hi' or 'assistant' in MyText:
                    s="Active"
                    SpeakText("I Woke ....... Waiting for your command boss  ")
                    print("I Woke ....... Waiting for your command boss  ")
          
                
          

     except sr.RequestError as e:
       print("Could not request results; {0}".format(e))
      
     except sr.UnknownValueError:
       print("",end="")
    
          
       #environment DA
       #take a picture

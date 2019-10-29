import speech_recognition as sr  
import webbrowser
# get audio from the microphone                                                                       
r = sr.Recognizer()     

def assistant(command):
    "if statements for executing commands"
#open subreddit Reddit
    if 'notepad' in command:
       os.system("notepad")
        
    elif 'shutdown' in command:
        sofiaResponse('Bye bye Sir. Have a nice day')
        sys.exit()
#open website
    elif 'open' in command:
        #reg_ex = re.search('open (.+)', command)
        #if reg_ex:
        #   domain = reg_ex.group(1)
        #    print(domain)
        url = 'https://www.' + command
        webbrowser.open(url)
            
        

    elif 'notepad' in command:
        os.system("notepad")




import os
os.system("echo 'hello world'")


from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
def SpeakText(command):
    speak.Speak(command)


while(1):                                                    
 with sr.Microphone() as source:             
     r.adjust_for_ambient_noise(source, duration=3)                                                            
     print("Speak:")                                                                                   
     audio = r.listen(source)   
    
 try:
    #sofiaResponse(audio)
    print("You said " + r.recognize_google(audio))
    re="You said " + r.recognize_google(audio)
    SpeakText(re)
    assistant(r.recognize_google(audio))
 except sr.UnknownValueError:
    print("Could not understand audio")
 except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


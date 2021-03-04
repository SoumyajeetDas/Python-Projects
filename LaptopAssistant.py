# Modules Downloaded --
# speechrecognition
# pyaudio
# pywin32 - Text to Speech
# pyinstaller- Python file to .exe
# Weather API used from - https://openweathermap.org/

import pyttsx3
import requests
import json
from datetime import datetime,date
import time
import speech_recognition as sr
import webbrowser
import os
import random
import pywhatkit
import calendar
speak=pyttsx3.init('sapi5') # sapi5 provides two voices on windows male and female
                            #.init creates Instance of Text to Speech Engine
vocal=speak.getProperty('voices') # getproperty gets the list of voices.Voice object i.e. David and Zira supported by the driver
speak.setProperty('voice',vocal[1].id) # Adds the property here it adds the property that it will talk in female voice
                                        # vocal[1].id for Zira and vocal[0].id for David

def listen():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            speak.say("Speak Now")
            speak.runAndWait() 
            print('Listening......')
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source)
            command=listener.recognize_google(voice,language='en-in')
    except Exception :
        speak.say("Couldn't understand")
        speak.say('Sorry')
        speak.say('Please tell once more')
        speak.runAndWait() # All the commands are 1st queued up and then runAndWait() proccesses all the commands
        command = 'Nothing'
    return command





def wish():
    '''
    To wish to the user
    '''
    Hour=datetime.now().hour
    if(Hour>=5 and Hour<=11):
        return 'Good Morning'
    elif(Hour>=12 and Hour<=16):
        return 'Good Afternoon'
    elif(Hour>=17 and Hour<=19):
        return 'Good Evening'
    else:
        return 'Good Night'



def weatherreport():
    '''
    Determing the current weather condition
    '''
    r=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Chandannagar&appid=58aced8999bab58e22c7ec3338d791d8") #requests.get() is used to request data from website with a url and retrieve it .
                                                                                                                # r contains the info that is being requested
    # data=json.loads(r.content)     .content provides the raw bytes of the response payload
    data=json.loads(r.text)  # .text convert the payload into JSON string using the character encoding UTF-8
                                # json.loads parses the JSON string into Python dictionary

# The whole Python dict is present in the data
    weather=data['weather'][0]['main']
    print("Climatic Condition :",weather)
    speak.say(f"Climatic condition is {weather}")
    speak.runAndWait()
    temp=int(data['main']['temp']-273.15)
    print(f"Temperature : {temp}°C")
    feeltemp=int(data['main']['feels_like']-273.15)
    print(f"Feels Like : {feeltemp}°C")
    speak.say(f"Temperature is {temp} degree celcius but feels like {feeltemp} degree celcius")
    speak.runAndWait()
    humidity=data['main']['humidity']
    print(f"Humidity : {humidity}%")
    speak.say(f"Humidity is {humidity} percent")
    speak.runAndWait()






def temperature():
    '''
    Determining today's temperature
    '''
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Chandannagar&appid=58aced8999bab58e22c7ec3338d791d8")
    data = json.loads(r.text)
    weather = data['weather'][0]['main']
    temp = int(data['main']['temp'] - 273.15)
    print(f"Temperature : {temp}°C")
    feeltemp = int(data['main']['feels_like'] - 273.15)
    print(f"Feels Like : {feeltemp}°C")
    speak.say(f"Temperature is {temp} degree celcius but feels like {feeltemp} degree celcius")
    speak.runAndWait()




def dates():
    '''
    Determining today's date
    '''
    day=date.today().day
    dictmonth={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    a=date.today().month
    month=dictmonth[a]
    year=date.today().year
    if(day==1):
        print(f"{day}st of {month} {year}")
        speak.say(f"Today is {day}st of {month} {year}")
        speak.runAndWait()
    elif(day==2):
        print(f"{day}nd of {month} {year}")
        speak.say(f"Today is {day}nd of {month} {year}")
        speak.runAndWait()
    elif(day==3):
        print(f"{day}rd of {month} {year}")
        speak.say(f"Today is {day}rd of {month} {year}")
        speak.runAndWait()
    else:
        print(f"{day}th of {month} {year}")
        speak.say(f"Today is {day}th of {month} {year}")
        speak.runAndWait()



def daying():
    '''
    Determining today's day
    '''
    
    dat=date.today().day
    month=date.today().month
    year=date.today().year

    d=calendar.weekday(year,month,dat)
    li=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    print(f"Today is {li[d]}")
    speak.say(f"Today is {li[d]}")
    speak.runAndWait()



def timing():
    '''
    Determining current time
    '''
    t=time.localtime()
    hour=int(time.strftime("%H",t))
    min=int(time.strftime("%M",t))

    if hour>12:
        hour=hour-12
        if hour==1:
            speak.say(f"It's {hour} our {min} minutes")
            print(f"{hour} hour {min} minutes")
            speak.runAndWait()
        else:
            speak.say(f"It's {hour} ours {min} minutes")
            print(f"{hour} hours {min} minutes")
            speak.runAndWait()
    elif hour==0:
        hour+=12
        speak.say(f"It's {hour} ours {min} minutes ")
        print(f"{hour} hours {min} minutes")
        speak.runAndWait()
    else:
        if hour==1:
            speak.say(f"It's {hour} our {min} minutes")
            print(f"{hour} hour {min} minutes")
            speak.runAndWait()
        else:
            speak.say(f"It's {hour} ours {min} minutes")
            print(f"{hour} hours {min} minutes")
            speak.runAndWait()





    

def ListenandContinueListen():
    k=listen()
    if(k=='Nothing'):
        while True:
            if(k=='Nothing'):
                k=listen()
            else:
                break
    return k



def listcando():
    '''
    Tells what Lappy can do for you
    '''
    speak.say('I can provide you with')
    speak.say("Weather Report")
    print("1. Weather Report")
    speak.say("Todays date day and time")
    print("2. Today's Date day and time")
    speak.say("Opening of github Spotify google youtube word excel powerpoint")
    print("3. Opening of Github Spotify Google Youtube Word Excel Powerpoint")
    speak.say("Listening to music")
    print("4. Listening to music")
    speak.say("Searching anything on youtube or search any song on youtube")
    print("5. Searching anything on youtube or search any song on youtube")
    speak.say("Searching anything on google")
    print("6. Searching anything on google")
    speak.runAndWait()




l=wish()
if l=='Good Morning':
    speak.say('Good Morning')
    speak.runAndWait()
elif l=='Good Afternoon':
    speak.say('Good Afternoon')
    speak.runAndWait()
elif l=='Good Evening':
    speak.say('Good Evening')

speak.say("Hi I am Lappy")





listcando()

speak.say("So what do you want me to do?")
speak.runAndWait()

count=0

'''
for the 1st time when program runs count=0 and program will run and for the next time when count>0 it will ask whether anything will be 
asked and if no is said it will go out of while loop
'''


while True:
    if(count==0):
        k=ListenandContinueListen()
        k=k.lower()

        if 'weather' in k:
            weatherreport()
            print("========================================================================")
            count+=1

        elif 'time' in k:
            timing()
            print("========================================================================")
            count += 1


        elif 'temperature' in k:
            temperature()
            print("========================================================================")
            count += 1

        elif 'date' in k:
            dates()
            print("========================================================================")
            count+=1


        elif 'day' in k or 'de' in k:
            daying()
            print("========================================================================")
            count += 1

        elif 'spotify' in k:
            print("Opening Spotify for you")
            speak.say("Opening Spotify for you")
            speak.runAndWait()
            webbrowser.open('https://open.spotify.com/')
            print("========================================================================")
            count+=1

        elif 'open google' in k :

            print("Opening Google for you")
            speak.say("Opening Google for you")
            speak.runAndWait()
            webbrowser.open('https://www.google.co.in/?gfe_rd=cr&ei=qtaZWafhEeSK8QeOxayICQ')
            print("========================================================================")
            count+=1

        elif 'open youtube' in k:
            print("Opening Youtube for you")
            speak.say("Opening Youtube for you")
            speak.runAndWait()
            webbrowser.open('https://www.youtube.com/')
            print("========================================================================")
            count+=1

        elif 'music' in k:
            print("Opening Music for you")
            speak.say("Opening Music for you")
            speak.runAndWait()
            dir='D:\\Music'
            songs=os.listdir(dir)
            k=random.randint(0,567)
            os.startfile(os.path.join(dir,songs[k]))
            count+=1
            print("========================================================================")
            
        elif 'word' in k:
            print("Opening Word for you")
            speak.say("Opening Word for you")
            speak.runAndWait()
            path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word'
            os.startfile(path)
            count+=1
            print("========================================================================")

        elif 'excel' in k:
            print("Opening Excel for you")
            speak.say("Opening Excel for you")
            speak.runAndWait()
            path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel'
            os.startfile(path)
            count+=1
            print("========================================================================")

        elif 'powerpoint' in k:
            print("Opening Powerpoint for you")
            speak.say("Opening Powerpoint for you")
            speak.runAndWait()
            path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint'
            os.startfile(path)
            count+=1
            print("========================================================================")
     
        elif 'search on youtube song' in k:
            k = k.replace('search on youtube', '')
            try:
                print('Searching.......')
                speak.say('Searching PLease wait')
                speak.runAndWait()
                pywhatkit.playonyt(k)
            except:
                print('An error occured')
                speak.say('An error occured')
                speak.say('Sorry')
                speak.runAndWait()
            count+=1
            print("========================================================================")

        elif 'search on youtube' in k:
            k = k.replace('search on youtube', '')
            try:
                print('Searching.......')
                speak.say('Searching PLease wait')
                speak.runAndWait()
                pywhatkit.playonyt(k)
            except:
                print('An error occured')
                speak.say('An error occured')
                speak.say('Sorry')
                speak.runAndWait()
            count+=1
            print("========================================================================")

        elif 'search on google' in k:
            k = k.replace('search on google', '')
            try:
                print('Searching.......')
                speak.say('Searching PLease wait')
                speak.runAndWait()
                pywhatkit.search(k)
            except:
                print('An error occured')
                speak.say('An error occured')
                speak.say('Sorry')
                speak.runAndWait()
            print("========================================================================")
            count+=1

        elif 'search for' in k:
            k = k.replace('search for', '')
            try:
                print('Searching.......')
                speak.say('Searching PLease wait')
                speak.runAndWait()
                speak.runAndWait()
                pywhatkit.search(k)
            except:
                print('An error occured')
                speak.say('An error occured')
                speak.say('Sorry')
                speak.runAndWait()
            print("========================================================================")
            count+=1

        elif 'search' in k:
            k = k.replace('search', '')
            try:
                print('Searching.......')
                speak.say('Searching PLease wait')
                speak.runAndWait()
                pywhatkit.search(k)
            except:
                print(k)
                print('An error occured')
                speak.say('An error occured')
                speak.say('Sorry')
                speak.runAndWait()
            print("========================================================================")
            count+=1

        elif 'open github' in k:
            print("Opening Github for you")
            speak.say("Opening Github for you")
            speak.runAndWait()
            webbrowser.open('https://github.com/')
            print("========================================================================")
            count+=1



        else:
            speak.say("Sorry I don't know how to do that")
            print("========================================================================")
            speak.runAndWait()
            count+=1



    else:
        speak.say('Anything else?')
        speak.say('Just Say Yes or No')
        speak.runAndWait()
        print('Yes or No')
        k=ListenandContinueListen()
        k=k.lower()

        if(k=='yes'):
            listcando()
            speak.say('So What can I do for you?')
            speak.runAndWait()
            p=ListenandContinueListen()
            p=p.lower()


            if 'weather' in p:
                weatherreport()
                print("========================================================================")

            elif 'time' in p:
                timing()
                print("========================================================================")


            elif 'temperature' in p:
                temperature()
                print("========================================================================")

            elif 'date' in p:
                dates()
                print("========================================================================")

            elif 'day' in p or 'de' in p:
                daying()
                print("========================================================================")

            elif 'spotify' in p:
                print("Opening Spotify for you")
                speak.say("Opening Spotify for you")
                speak.runAndWait()
                webbrowser.open('https://open.spotify.com/')
                print("========================================================================")

            elif 'open google' in p:
                print("Opening Google for you")
                speak.say("Opening Google for you")
                speak.runAndWait()
                webbrowser.open('https://www.google.co.in/?gfe_rd=cr&ei=qtaZWafhEeSK8QeOxayICQ')
                print("========================================================================")

            elif 'open youtube' in p:
                print("Opening Youtube for you")
                speak.say("Opening Youtube for you")
                speak.runAndWait()
                webbrowser.open('https://www.youtube.com/')
                print("========================================================================")

            elif 'music' in p:
                print("Opening Music for you")
                speak.say("Opening Music for you")
                speak.runAndWait()
                dir='D:\\Music'
                songs=os.listdir(dir)
                k=random.randint(0,567)
                os.startfile(os.path.join(dir,songs[k]))
                print("========================================================================")

            elif 'word' in p:
                print("Opening Word for you")
                speak.say("Opening Word for you")
                speak.runAndWait()
                path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word'
                os.startfile(path)
                print("========================================================================")

            elif 'excel' in p:
                print("Opening Excel for you")
                speak.say("Opening Excel for you")
                speak.runAndWait()
                path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel'
                os.startfile(path)
                print("========================================================================")

            elif 'powerpoint' in p:
                print("Opening Powerpoint for you")
                speak.say("Opening Powerpoint for you")
                speak.runAndWait()
                path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint'
                os.startfile(path)
                print("========================================================================")

            elif 'search on youtube' in p:
                p=p.replace('search on youtube','')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.playonyt(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")

            elif 'search on youtube song' in p:
                p=p.replace('search on youtube song','')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.playonyt(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")
            
            elif 'search on youtube' in p:
                p=p.replace('search on youtube','')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.playonyt(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")

            elif 'search on google' in p:
                p=p.replace('search on google','')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.search(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")

            elif 'search for' in p:
                p = p.replace('search for', '')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.search(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")

            elif 'search' in p:
                p=p.replace('search','')
                try:
                    print('Searching.......')
                    speak.say('Searching PLease wait')
                    speak.runAndWait()
                    pywhatkit.search(p)
                except:
                    print('An error occured')
                    speak.say('An error occured')
                    speak.say('Sorry')
                    speak.runAndWait()
                print("========================================================================")
            
            elif 'open github' in p:
                print("Opening Github for you")
                speak.say("Opening Github for you")
                speak.runAndWait()
                webbrowser.open('https://github.com/')
                print("========================================================================")
                count+=1

            else:

                speak.say("Sorry I don't know how to do that")
                print("========================================================================")
                speak.runAndWait()
            count+=1


        elif(k=='no'):
            speak.say('ok Thank You')
            speak.say("Nice Talking To You")
            speak.say('Good Bye')
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            speak.runAndWait()
            break



l=wish()
if(l=='Good Night'):
    speak.say("Good Night")
    speak.runAndWait()








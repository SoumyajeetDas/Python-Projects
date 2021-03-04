import requests
import json

from win32com.client import Dispatch

speak=Dispatch("SAPI.SpVoice") # Converts text to speech. It interacts with Microsoft Speech SDK
speak.Speak("Hi Soumyajeet !!")
speak.Speak("Hope you are doing Well")
speak.Speak("Do you want me to read news?")
speak.Speak("Please type your response")
o=input('Enter the input : ')


if o == 'Yes':
    speak.speak("Reading News")
    r=requests.get('http://newsapi.org/v2/top-headlines?' # requests.get() is used to request data from website with a url and retrieve it .            
       'country=us&'                                      # r contains the information sent by requests.get() known as payload
       'apiKey=8a70a5db855043808dbc69df5d02f374')
    # data=json.loads(r.content)     .content provides the raw bytes of the response payload 
    data=json.loads(r.text) # .text convert the payload into string using the character encoding UTF-8 
                            # json.loads parses the JSON string into Python dictionary
        # The whole Python dictionary is present within data


    for i in range(1,6):

        if(i==1):
            speak.Speak(f"{i}st news")
            speak.Speak(data['articles'][i]['title'])
        elif(i==2):
            speak.Speak(f"{i}nd news")
            speak.Speak(data['articles'][i]['title'])
        elif(i==3):
            speak.Speak(f"{i}rd news")
            speak.Speak(data['articles'][i]['title'])
        else:
            speak.Speak(f"{i}th news")
            speak.Speak(data['articles'][i]['title'])
    else:
        speak.Speak("Thank You")
        

else:
    speak.Speak("Sad to here No from you")
    speak.Speak("Thank You")

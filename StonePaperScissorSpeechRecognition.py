# Modules Downloaded --
# speechrecognition
# pyaudio
# pywin32 - Text to Speech
# pyinstaller- Python file to .exe



import random
from win32com.client import Dispatch
import speech_recognition as sr

speak = Dispatch("SAPI.SpVoice") # Converts text to speech. It interacts with Microsoft Speech SDK

speak.Speak('Hi')
speak.Speak('Lets Play Stone Paper Scissor!!')





'''
In Listen() function first Recognizer class is called 
Then Microphone is used as source
Then speech is listened that is input from microphone
Then the speech is recognized by google Speech API and then convert into text or string format
If it cannot recognize it will throw an Error and will go to except block
'''



# variables for calculating score of computer as well as the player
scoreyou=0
scorecomputer=0






def Listen():
    listener = sr.Recognizer() # Recognizer Class instance is created  to perform different speech operations. Recognizer() is the object and since it is called from different module sr is used
    try:
        with sr.Microphone() as source: # Using class Microphone instance it uses the computer microphone to use it as a source to listen
            speak.Speak("Speak Now")
            print('Listening...')
            voice = listener.listen(source) # Listen the input from Microphone Listen is an instance of Recognizer class
            command = listener.recognize_google(voice, language='en-in') # Google Speech API converts the speech to text. 
                                                    # If google cannot recognize as english word it will throw an exception
    except Exception as e:
        speak.Speak('Couldnt Understand')
        speak.Speak('Sorry')
        speak.Speak('Please tell once more')
        command='Nothing'   # Since nothing present in command so command will contain 'Nothing' --> command='Nothing'
    return command







def compute(comp, you):   # Check the result between you and computer and returns who is the winner
        if (comp == you):
             return 'same'
        elif (comp == 's' and (you == 'a' or you == 'A')):
            return 'you'
        elif (comp == 'a' and (you == 's' or you == 'S')):
            return 'comp'
        elif (comp == 's' and (you == 'I' or you == 'i')):
            return 'comp'
        elif (comp == 'I' and (you == 's' or you == 'S')):
            return 'you'
        elif (comp == 'a' and (you == 'I' or you == 'i')):
            return 'you'
        elif (comp == 'I' and (you == 'a' or you == 'A')):
            return 'comp'
        else:
            return 'Wrong'







def computeforcomp(comp): # To compute what the computer has taken
    if (comp=='s'):
        return 'Stone'
    elif(comp=='I'):
        return 'Scissor'
    elif(comp=='a'):
        return 'Paper'








def computeforyou(you): # To compute what you have taken
    if (you=='s'):
        return 'Stone'
    elif(you=='I'):
        return 'Scissor'
    elif(you=='a'):
        return 'Paper'







def computescore(scoreyou,scorecomputer): # Computes who won at last computer or you
    if(scoreyou>scorecomputer):
        speak.Speak(f"Computer Scored {scorecomputer} and you scored {scoreyou} finally")
        speak.Speak('So You are the final winner')
    else:
        speak.Speak(f"Computer Scored {scorecomputer} and you scored {scoreyou} finally")
        speak.Speak('Computer is the final winner')









def ListenOrContineListen(): # If it cannot recognize it will throws error and return 'Nothing' and when it will get other than 'Nothing' it will come out of the loop 
    p = Listen()  # and will return the speech which is recognized
    if(p=='Nothing'):
        while True:
            if(p=='Nothing'):
                p=Listen()
            else:
                break
    return p







while True:
    speak.Speak('Do you want to play ?')
    speak.Speak("Tell Yes or No")

    k=ListenOrContineListen()


    if (k == 'Yes' or k == 'yes'):
        speak.Speak('You have opted to play')

        

        comp = random.randint(1, 3)
        if (comp == 1):
            comp = 's'
            speak.Speak('I have opted')
            speak.Speak('Now its your turn')
            speak.Speak('What will you opt for ?')
        elif (comp == 2):
            comp = 'I'
            speak.Speak('I have opted')
            speak.Speak('Now its your turn')
            speak.Speak('What will you opt for ?')

        elif (comp == 3):
            comp = 'a'
            speak.Speak('I have opted')
            speak.Speak('Now its your turn')
            speak.Speak('What will you opt for ?')
        

        


        speak.Speak('Stone Paper or Scissor')
        print('Tell I for Scissor S for stone and A for Paper')
        speak.Speak('Tell I for Scissor S for stone and A for Paper')





        computer=computeforcomp(comp)

        you=ListenOrContineListen()

        foryou=computeforyou(you)




        
        
        l = compute(comp, you)
        if (l == 'same'):
            print(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak('So None of you won')
            print(f"Your's Score : {scoreyou}")
            print(f"Computer Score : {scorecomputer}")
            speak.Speak(f"Your score is {scoreyou} and computer's score is {scorecomputer}")
            speak.Speak("Thank You")
            print("===============================================================")


        elif (l == 'you'):
            scoreyou+=1
            print(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak('You won')
            speak.Speak('Congratulations !!')
            print(f"Your's Score : {scoreyou}")
            print(f"Computer Score : {scorecomputer}")
            speak.Speak(f"Your score is {scoreyou} and computer's score is {scorecomputer}")
            speak.Speak("Thank You")
            print("===============================================================")


        elif (l == 'comp'):
            scorecomputer+=1
            print(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak(f"Computer opted for {computer} and you have opted for {foryou}")
            speak.Speak('Computer Won')
            speak.Speak('Better Luck Next Time !!')
            print(f"Your's Score : {scoreyou}")
            print(f"Computer Score : {scorecomputer}")
            speak.Speak(f"Your score is {scoreyou} and computer's score is {scorecomputer}")
            speak.Speak("Thank You")
            print("===============================================================")


        else:
            speak.Speak('Wrong Input')

    



    elif (k == 'No' or k == 'no'):
        speak.Speak('Ok')
        print("Final Score------")
        print("Computer Score : ",scorecomputer)
        print("Your's Score : ",scoreyou)
        computescore(scoreyou,scorecomputer)
        speak.Speak('Nice to play with you !!')
        speak.Speak('We will again play afterwards')
        speak.Speak('Bye')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        break



    else:
        speak.Speak("Wrong Input")

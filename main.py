import speech_recognition as sr
import pyttsx3 as pt
import datetime
import pywhatkit
import wikipedia
import pyjokes

listner = sr.Recognizer()
alexa = pt.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
def talk(text):
    alexa.say(text)
    alexa.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listning.....')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)



    except:
        pass
    return command

def run_alexa():
        command = take_command()
        if 'time' in command:
            time =datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is'+time)

        elif 'tell me about' in command:
            look_for = command.replace('tell me about','')
            info = wikipedia.summary(look_for, 1)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'date' in command:
            talk('Sorry vaiya! I have a boyfriend')
        else:
            talk("Please tell me again!")
            # pywhatkit.search(command)

        # elif 'play' in command:
        #     song = command.replace('play ', '')
        #     talk('playing ' + song)
        #     pywhatkit.playonyt(song, use_api=True)



run_alexa()


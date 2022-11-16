import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as w
import pyjokes


engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    fecha = ()
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    fecha = (day,  month, year)
    speak("Today is: ")
    speak(fecha)
    
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The times is: ")
    speak(time)

def greeting():
    speak("Welcome! I'm Riley")

    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        speak("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")

    speak("How can i help you?")

def takecommmand():
    r = sr.Recognizer() 
 
    with sr.Microphone() as source:
        print('Speak Anything : ')
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognising...")
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))

    except:
        speak('Sorry could not hear')

    return text

def jokes():
    speak(pyjokes.get_joke())



if __name__ == '__main__':

    greeting()

    while True:
        query = takecommmand()
        print(query)

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif "search" in query:
            speak("Searching...")
            query = query.replace("search", "")
            result = w.summary(query, sentences = 2)
            speak(result)

        elif 'joke' in query:
            speak("Here's a joke for you: ")
            jokes()

        elif 'turn off' in query:
            speak("Goodbye!")
            quit()
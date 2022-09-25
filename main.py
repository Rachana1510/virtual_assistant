#importing packages
import pywhatkit
import speech_recognition as sr
import pyttsx3 as tts
import datetime
import pyjokes
#object declarations
listener = sr.Recognizer()
converter = tts.init()
#setting voice to engine
voice_array = converter.getProperty('voices')
converter.setProperty('voice', voice_array[2].id)
#function to talk
def talk(text):
    converter.say(text)
    converter.runAndWait()
#function to run
def run(command):
   if "siri" in command:
       command=command.replace("siri","")
       if "play" in command:
           song = command.replace("play","")
           talk("playing..."+song)
           # assert isinstance(song, object)
           pywhatkit.playonyt(song)
       elif "recipe" in command:
           recipe = command.replace("recipe","")
           talk("loading your search")
           pywhatkit.playonyt(recipe)
       elif "make" in command:
           talk("loading your search")
           pywhatkit.playonyt(command)
       elif "search" in command:
           srch = command.replace("search","")
           talk("searching for"+srch)
           pywhatkit.search(srch)
       elif "joke" in command:
           joke = pyjokes.get_joke(language="en", category="neutral")
           print(joke)
           talk(joke)
       elif "date" in command:
           date = datetime.datetime.now().strftime("The DATE is:%d-%B-%Y")
           print(date)
           talk(date)
       elif "time" in command:
           time = datetime.datetime.now().strftime("The TIME is:%H:%M %p")
           print(time)
           talk(time)
   else:
        raise sr.RequestError
try:
    with sr.Microphone() as origin:
        print("Listening.....")
        talk("listening")
        mic = listener.listen(origin, timeout=5)
        order = listener.recognize_google(mic)
        order = order.lower()
        print(order)
        run(order)
        #if "siri" in order:
            # order=order.replace("siri"," ")
            #print(order)
            #run(order)
        #else:
        #     raise sr.RequestError

except sr.WaitTimeoutError as timeout:
    print("could you please speak again!")
    talk("could you please speak again!")
except sr.UnknownValueError as unknown:
    print("couldn't get you, could you speak again")
    talk("couldn't get you, could you speak again")
except sr.RequestError as request_error:
    print("try saying siri in your command")
    talk("try saying siri in your command")

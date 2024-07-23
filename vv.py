import pyttsx3
# import speech_recognition as sr
import datetime
import googletrans
import speech_recognition
import gtts
# import playsound

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# recognizer = speech_recognition.Recognizer()
# with speech_recognition.Microphone() as source:
#     print("Speak Now !!....")
#     voice = recognizer.listen(source)       
#     text = recognizer.recognize_google(voice,language="fr")
#     print(text)


# translater=googletrans.Translator()
# translation=translater.translate(text,dest="fr")
# print(translation.text)

# Converted_audio = gtts.gTTS(translation.text,lang="fr")
# Converted_audio.save("Hellow.mp3")
# playsound.playsound("Hellow.mp3")
#print(googletrans.LANGUAGES)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am jarvis , how can i help you !! ")

def takeCommand():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Speak Now !!....")
        voice = recognizer.listen(source)       
        text = recognizer.recognize_google(voice,language="en-in")
        print(text)
    # r=sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     # r.pause_threshold=1
    #     audio=r.listen(source)

    # # try:
    #     print("Recogrizing...")
    #     query=r.recognize_google(audio,Language='en-in')
    #     print(f"user said : {query}\n")
    
    # except Exception as e:
    #     # print(e)

    #     print("Say that again ")
        # return "None"
    
    # return query


# if __name__=="__main__":
    # Wishme()
    
takeCommand()
    # speak("Hi")
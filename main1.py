import googletrans
import speech_recognition
import gtts
import playsound

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now !!....")
    voice = recognizer.listen(source)       
    text = recognizer.recognize_google(voice,language="fr")
    print(text)


translater=googletrans.Translator()
translation=translater.translate(text,dest="fr")
print(translation.text)

Converted_audio = gtts.gTTS(translation.text,lang="fr")
Converted_audio.save("Hellow.mp3")
playsound.playsound("Hellow.mp3")
# print(googletrans.LANGUAGES)

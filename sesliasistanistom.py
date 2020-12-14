import speech_recognition as sr
import time 
import random
import os
from gtts import gTTS
from playsound import playsound
import random
import os
r  = sr.Recognizer()
def kayit():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = " "
        try:
            voice = r.recognize_google(audio, language = 'tr-TR')
        except sr.UnknownValueError:
            speak("anlayamadim")
        except sr.RequestError:
            speak("sistem calismiyor")
        return(voice)
def response(voice):
    if "nasılsın" in voice:
        speak("iyi senden")
    if "Selam" in voice:
        speak("Selam")
    if "tamamdır" in voice:
        speak("görüşürüz")
    if "hangi yıldayız" in voice:
        speak("2020")
    if "kahve" in voice:
        speak("bir fincan kahve olsam")    
        exit()
def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio='+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("nasıl yardımcı olabilirim")
voice = kayit()
print(voice)
response(voice)
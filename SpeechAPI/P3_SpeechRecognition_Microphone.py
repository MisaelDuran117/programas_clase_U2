import speech_recognition as sr
import os

if not os.path.exists("audios"):
    os.mkdir("audios")

r = sr.Recognizer()
print("Iniciada")
audio_file =sr.AudioFile("audios/audio_fie.wav")

try:
    with audio_file as source:
        audio=r.record(source)
    cadena = r.recognize_google(audio, language="es-MX",show_all=True)
    print("Mensaje: ")
    print(cadena)

except sr.UnknownValueError:
    print("Unknow Value Error")
except sr.RequestError as e:
    print("Request Error: {}".format(e))
except Exception as ex:
    print("Error: {}".format(ex))
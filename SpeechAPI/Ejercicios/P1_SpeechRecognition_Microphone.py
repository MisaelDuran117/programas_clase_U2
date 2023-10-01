import speech_recognition as sr
r=sr.Recognizer()

print("Iniciada")
with sr.Microphone() as source:
    audio=r.listen(source)

print("Registro Generado")

try:
    cadena= r.recognize_google(audio,language="es-MX")
    print("Mensaje: " + cadena)
except sr.UnknownValueError:
    print("Unknow Value Error")
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print("Error: ".format(ex))
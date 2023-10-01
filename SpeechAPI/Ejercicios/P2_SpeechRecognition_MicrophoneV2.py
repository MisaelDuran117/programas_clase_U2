import speech_recognition as sr
r=sr.Recognizer()
print("inicia:")
with sr.Microphone() as source:
    audio=r.listen(source)

    print("Registro Generado!:")
with open("audios/audio_fie.wav", "wb") as file:
    file.write(audio.get_wav_data())
print("Archivo Creado!")
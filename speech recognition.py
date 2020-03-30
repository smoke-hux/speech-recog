import speech_recognition as sr
import pprint
import sys
pprint.pprint(sys.path)
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything: ')
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print('You said : {}'.format(text))
    try:
        text= r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Sory could not recognize your voice')
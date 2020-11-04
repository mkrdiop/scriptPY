#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:23:30 2019

@author: makhtardiop

"""
#!/usr/bin/env python3

import speech_recognition as sr
import sys
# obtain path to "english.wav" in the same folder as this script

if sys.argv[1]=='fr':
    lang="fr-FR"
if sys.argv[1]=='en':
    lang="en-EN"
    
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "buy3.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    print ("recording file")
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio, language=lang))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


"""
import speech_recognition as sr     # import the library
harvard = sr.AudioFile('buy.wav')
with harvard as source:
    audio = r.record(source)
 

r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
"""
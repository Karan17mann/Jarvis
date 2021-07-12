import pyttsx3
import speech_recognition as sr #making an import
import datetime
import wikipedia
import os
import smtplib
print("HELLO")

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("HELLO mr MAAN")

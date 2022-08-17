# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

root = Tk()
root.config(bg='black')
root.geometry("1200x800")
root.title("Hackerzzz / ANY.")

microphoneImg = ImageTk.PhotoImage(Image.open("Microphone.png"))

img = Label(root, bg='black', fg='white', image=microphoneImg, text="")
img.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()



def code():


    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    
    def talk(text):
        engine.say(text)
        engine.runAndWait()
    
    
    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source, phrase_time_limit=(5))
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
        except:
            pass
        return command
    
    
    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        else:
            talk('Please say the command again.')
    
    
    run_alexa()
















code()









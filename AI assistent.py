# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio
import pyjokes
import pywhatkit
from tkinter import filedialog



root = Tk()
root.geometry("500x500")
root.title("Assistance")
root.config(bg="black")

def codeAI():
    root.destroy()

    assistant = Tk()
    assistant.config(bg='black')
    assistant.title('ANY.')
    assistant.geometry("600x650")


    

    print('Loading your AI personal assistant')






    def code():
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice','voices[0].id')


        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def wishMe():
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<12:
                speak("Hello,Good Morning. How may I help you?")
                print("Hello,Good Morning. How may I help you?")
            elif hour>=12 and hour<18:
                speak("Hello,Good Afternoon. How may I help you?")
                print("Hello,Good Afternoon. How may I help you?")
            else:
                speak("Hello,Good Evening. How may I help you?")
                print("Hello,Good Evening. How may I help you?")

        

        def takeCommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source)

                try:
                    statement=r.recognize_google(audio,language='en-in')
                    print(f"user said:{statement}\n")
                    userInput['text']="user said: " + statement
                    

                except Exception as e:
                    speak("Pardon me, please say that again")
                    return "None"
                return statement


        wishMe()


        if __name__=='__main__':


            while True:
                statement = takeCommand().lower()
                if statement==0:
                    continue

                if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                    speak('your personal assistant is shutting down,Good bye')
                    print('your personal assistant is shutting down,Good bye')
                    break



                elif 'wikipedia' in statement:
                    webbrowser.open_new_tab("https://www.wikipedia.org/")
                    speak("Wikipedia is open now")
                    time.sleep(5)

                

                elif 'open gmail' in statement:
                    webbrowser.open_new_tab("https://www.gmail.com")
                    speak("Google Mail open now")
                    time.sleep(5)

                elif "weather" in statement:
                    api_key="8ef61edcf1c576d65d836254e11ea420"
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    speak("whats the city name")
                    city_name=takeCommand()
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" Temperature in kelvin unit is " +
                              str(current_temperature) +
                              "\n humidity in percentage is " +
                              str(current_humidiy) +
                              "\n description  " +
                              str(weather_description))
                        
                        print(" Temperature in kelvin unit = " +
                              str(current_temperature) +
                              "\n humidity (in percentage) = " +
                              str(current_humidiy) +
                              "\n description = " +
                              str(weather_description))
                        output['text']=" Temperature in kelvin unit = "+str(current_temperature)+"\n humidity (in percentage) = "+str(current_humidiy)+"\n description = "+str(weather_description)

                    else:
                        speak(" City Not Found ")



                elif 'time' in statement:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                    output['text']="The time is"+strTime

                elif 'who are you' in statement or 'what can you do' in statement:
                    speak('I am your persoanl assistant. I am programmed to minor tasks like'
                          'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                          'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
                    output['text']="I am your persoanl assistant. I am programmed to minor tasks like opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!"
                         


                elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I was built by the Hackerzzz")
                    print("I was built by the Hackerzzz")
                    output['text']="I was built by the Hackerzzz"

                elif "open stackoverflow" in statement:
                    speak("Opening stackoverflow")
                    output['text']="Opening stackoverflow"
                    webbrowser.open_new_tab("https://stackoverflow.com/login")
                    

                elif 'news' in statement:
                    speak('Here are some headlines from the Times of India,Happy reading')
                    output['text']="Here are some headlines from the Times of India. Happy reading"
                    news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                    time.sleep(6)
                    
                elif 'open spotify' in statement:
                    speak('Opening Spotify')
                    output['text']="Opening Spotify"
                    news = webbrowser.open_new_tab("https://open.spotify.com/")
                    


                elif 'search'  in statement:
                    statement = statement.replace("search", "")
                    output['text']="Searching..."
                    webbrowser.open_new_tab(statement)
                    time.sleep(5)

                elif 'ask' in statement:
                    speak('I can answer to computational and geographical questions and what question do you want to ask now')
                    question=takeCommand()
                    app_id="R2K75H-7ELALHR35X"
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)


                elif "log off" in statement or "sign out" in statement or "shut down" in statement:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    output['text']="Logging off"
                    time.sleep(10)
                    subprocess.call(["shutdown", "/l"])
                
                elif 'play' in statement:
                    song = statement.replace('play', '')
                    output['text']="Playing"+song
                    speak('playing ' + song)
                    pywhatkit.playonyt(song)
                    
                
                    
                elif 'who is' in statement:
                    person = statement.replace('who is', '')
                    info = wikipedia.summary(statement)
                    output['text']=info
                    print(info)
                    speak(info)
                    
                elif 'are you single' in statement:
                    speak('I am in a relationship with wifi')
                    output['text']="I am in a relationship with wifi"
                    
                elif 'joke' in statement:
                    print(pyjokes.get_joke())
                    talk(pyjokes.get_joke())
                    
                elif 'open youtube' in statement:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    output['text']="Opening youtube"
                    speak("Opening youtube")
                    
                elif 'open google' in statement:
                    speak("Opening Google chrome")
                    output['text']="Opening google chrome"
                    webbrowser.open_new_tab("https://www.google.com")
                    

        time.sleep(3)


    
    
        

    btn = Button(assistant, text="Start", bg="purple", fg="white", command=code)
    btn.place(relx=0.5, rely=0.2, anchor=CENTER)

    userInput = Label(assistant, bg="black", fg="white", text="User said: ", width=200)
    userInput.place(relx=0.5, rely=0.4, anchor=CENTER)

    output = Label(assistant, bg="black", fg="white", width=200)
    output.place(relx=0.5, rely=0.5, anchor=CENTER)

    
    assistant.mainloop()
    
def codeST():
    root.destroy()

    StoT = Tk()
    StoT.geometry("1000x1000")
    StoT.config(bg="black")

    
    textToSpeech = pyttsx3.init()

    label = Label(StoT, text="Speech to Text", bg="black", fg="white", font=("Bahnschrift Light", 15, "bold"))
    label.place(relx=0.5, rely=0.1, anchor=CENTER)

    textarea = Text(StoT, bg="white", fg="black", relief=FLAT)
    textarea.place(relx=0.5, rely=0.5, anchor=CENTER)

    def speak(audio):
        textToSpeech.say(audio)
        textToSpeech.runAndWait()

    def sr_audio():
        speak("How can I help you..?")
        SR = sr.Recognizer()
        with sr.Microphone() as source:
            audio = SR.listen(source)
            voiceData = ''
            try:
                voiceData = SR.recognize_google(audio, language='en-in')
                print(voiceData)
                textarea.insert(END, " "+voiceData+".", END)
            except sr.UnknownValueError:
                print("Please repeat, I did not get that.")
                speak("Please repeat, I did not get that")
                
                

    btn = Button(StoT, text="Start", bg="Blue", fg="white", font=("Arial", 11, "bold"), relief=FLAT, command=sr_audio)
    btn.place(relx=0.5, rely=0.16, anchor=CENTER)



    StoT.mainloop()













btn1 = Button(root, bg="purple", fg="white", text="Speech to Text", command=codeST)
btn1.place(relx=0.3, rely=0.2, anchor=CENTER)

btn2 = Button(root, bg="purple", fg="white", text="AI Intelligence", command=codeAI)
btn2.place(relx=0.7, rely=0.2, anchor=CENTER) 

root.mainloop()

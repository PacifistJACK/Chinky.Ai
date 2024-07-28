import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import os
import requests
from groq import Groq
from datetime import datetime


# Initialize the recognizer and text-to-speech engine
reco = sr.Recognizer()
eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)
eng.setProperty('rate', 185)
#APIs
def get_news_headlines():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'in',
        'apiKey': '0beca6ef245e44eda9a87b6c7af52f0a'
     }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        for article in articles:
            speak(article['title'])
    else:
        speak("Failed to retrieve news")



# Function to speak a given text
def speak(t):
    eng.say(t)
    eng.runAndWait()

def aiprocess(command):
    client = Groq(api_key='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')
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": command
            }
        ],
        temperature=1,
        max_tokens=100,
        top_p=1,
        stream=True,
        stop=None,
    )

    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""
    
    return response_text


def processcmd(c):
    if "your name" in c.lower():
        speak(f"My Name is chinky")
    elif "open google" in c.lower():
        speak("Openning Google!")
        wb.open("www.google.com")
    elif "open instagram" in c.lower():
        speak("Openning Instagram!")
        wb.open("www.instagram.com")
    elif "open youtube" in c.lower():
        speak("Openning youtube!")
        wb.open("www.youtube.com")
    elif "spotify" in c.lower():
        speak("Opening Spotify!")
        os.startfile(r"C:\Users\utkar\AppData\Local\Microsoft\WindowsApps\Spotify.exe")
    elif "read news" in c.lower():
        speak("Fetching the latest news headlines!")
        get_news_headlines()
    elif "time" in c.lower():
        speak("Current Time is!")
        speak((datetime.now().strftime("%H:%M")))
    elif "date" in c.lower():
        speak("Today is!")
        speak(datetime.now().strftime(" %d %B, %A "))
    #Letting Other Response by AI
    else:
        response = aiprocess(c)
        print("Chori: " + response)
        speak(response)
        




if __name__ == "__main__":
    # Speak a test phrase
    speak("I am ready sir!")

    while True:

        # Create a recognizer instance
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Say something!")
            try:
                audio = r.listen(source, timeout=2)
                print("Evaluating...")
                
                # Recognize speech using Google's speech recognition
                command = r.recognize_google(audio)
                # print(f"You said: {command}")
                
                if command.lower() == "chinky":#fOR cOMMANDING Her
                    speak("Yes sir!")
                    with sr.Microphone() as source:
                        print("Ready!")
                        speak("What Can I do For You sir?")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(command)

                        processcmd(command)
                elif command.lower() == "stop":
                    speak("GoodBye sir! see you later.")
                    break
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
            except sr.UnknownValueError:
                print("Chorri couldn't understand")
            except sr.RequestError as e:
                print(f"BoomaBam Error {e}")
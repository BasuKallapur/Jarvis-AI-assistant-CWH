import speech_recognition as sr
import webbrowser
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python
import musicLib
import requests
# from openai import OpenAI
# pip install pocketsphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<your key here>"  # Replace with your News API key

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def aiprocess(command):
#         client = OpenAI(api_key="<put your api key>")
#         completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
#             {
#                 "role": "user",
#                 "content": "which is best programming language"
#             }
#         ]
#     )
#         print(completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # for example, if we say "play believer", output is ["play", "believer"]
        link = musicLib.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find the song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # parse the JSON articles
            data = r.json()
            # Extract the articles
            articles = data.get('articles', [])
            # print headlines
            for article in articles:
                speak(article['title']) 
        else:
            speak("Sorry, I couldn't retrieve the news.")
    else:
        # Let OpenAI handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True: 
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1) 
            word = recognizer.recognize_google(audio)
            if word.lower() == "hello":  # Say "hello" to activate Jarvis
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis activated...")
                    audio = recognizer.listen(source, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

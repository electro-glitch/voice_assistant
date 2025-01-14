import speech_recognition as speech
import requests
import google.generativeai as genai
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def summarize_search(query, search_api_key):
    cx = '23693f322c80a4ef5'
    response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={search_api_key}&cx={cx}&q={query}")
    search_results = response.json()

    links = []
    if 'items' in search_results:
        for item in search_results['items']:
            snippet = item.get('snippet', '')
            title = item.get('title', '')
            link = item.get('link', '')
            if snippet:
                links.append(f"Title: {title}\nLink: {link}\n")
    
    if links:
        return "\n\n".join(links)
    else:
        return "No relevant links found."

def narrate_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

def main():
    sound = speech.Recognizer()
    with speech.Microphone() as source:
        print("Say something:")
        audio = sound.listen(source)
    try:
        user_input = sound.recognize_google(audio)
        print(f"You said: {user_input}")
        
        summary = summarize_search(user_input, SEARCH_API_KEY)
        
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        print("Here are some links you can follow:\n", summary)
        
        prompt = f"Summarize the following content based on the query: '{user_input}'. Here is the content:\n{summary}. Keep in mind that the response should be informative, informal, concise and helpful. Basically like a mini voice assistant for the average person."
        ai_response = model.generate_content(prompt)
        
        print("AI Response based on search results:\n", ai_response.text)
        narrate_text(ai_response.text)
    except speech.UnknownValueError:
        print("Sorry, could not understand audio")

if __name__ == "__main__":
    main()
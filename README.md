# Voice Assistant🎙️

A simple voice assistant that listens to your commands, performs a web search, summarizes the results, and reads it back to you using text-to-speech. Powered by Google Gemini.

## Features🚀
- Recognizes speech input and convert it to text.
- Gives Gemini's response in text and proceeds to read it out aloud
- Returns a list of webpage links you might find useful based on the input

## Setup🏗️

1. **Clone the repo**:
   ```bash
   git clone https://github.com/itstanayhere/voice_assistant.git
   cd voice_assistant
2. **Create a**``.env`` **file**
   ```env
   SEARCH_API_KEY=your_search_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
3. **Install the dependencies using** ```pip```
   ```pip
   pip install speechrecogniton
   pip install urllib
   pip install google.generativeai
   pip install pyttsx3
   pip install python-dotenv
   
## Usage👍

To run the script, use the following command:

```bash
python voicesearch.py
```

Or just run it directly from your IDE!

The script will listen for your voice, search the web based on what you say, summarize the results, and speak the summary out loud.

## Notes
- You’ll need to sign up for your own API keys from Google Custom Search API and Gemini API.
- Make sure your microphone is working well for speech recognition! 

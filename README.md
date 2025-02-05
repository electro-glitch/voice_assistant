# Update (05/02/2025)
The code for the webscraper has also been removed from the repository.

# Update (28/1/2025)
Web scraping been separated from the main code owing to terms and conditions of various websites. Code now only gives relevant links and an AI generated summary of the search query.
# Voice Assistant

A simple voice assistant that listens to your commands, performs a web search, summarizes the results, and reads it back to you using text-to-speech.

## Features
- Recognize speech and convert it to text.
- Perform web searches using Google Custom Search API.
- Summarize the search results with Gemini API.
- Read the summary out loud with text-to-speech.

## Setup

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
   
## Usage

To run the script, use the following command:

```bash
python voicesearch.py
```

Or just run it directly from your IDE!

The script will listen for your voice, search the web based on what you say, summarize the results, and speak the summary out loud.

## Notes
- You’ll need to sign up for your own API keys from Google Custom Search API and Gemini API.
- Make sure your microphone is working well for speech recognition! 

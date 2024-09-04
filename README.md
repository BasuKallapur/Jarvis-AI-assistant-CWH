# Jarvis: Voice-Activated Virtual Assistant

Jarvis is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model.

## Features

- **Voice Recognition**  
  Utilizes the `speech_recognition` library to listen for and recognize voice commands.  
  Activates upon detecting the wake word **"Jarvis."**

- **Text-to-Speech**  
  - Converts text to speech using `pyttsx3` for local conversion.  
  - Uses `gTTS` (Google Text-to-Speech) and `pygame` for playback.

- **Web Browsing**  
  Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

- **Music Playback**  
  Interfaces with a `musicLibrary` module to play songs via web links.

- **News Fetching**  
  Fetches and reads the latest news headlines using the [NewsAPI](https://newsapi.org).

- **OpenAI Integration**  
  Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.  
  Acts as a general virtual assistant similar to Alexa or Google Assistant.

## Workflow

1. **Initialization**  
   Greets the user with "Initializing Jarvis..."

2. **Wake Word Detection**  
   Listens for the wake word **"Jarvis."**  
   Acknowledges activation by saying "Yes?"

3. **Command Processing**  
   Processes commands to determine actions such as opening a website, playing music, fetching news, or generating a response via OpenAI.

4. **Speech Output**  
   Provides responses using the `speak` function with either `pyttsx3` or `gTTS`.

## Libraries Used

- `speech_recognition` - For recognizing voice commands.
- `webbrowser` - For opening web pages.
- `pyttsx3` - For text-to-speech conversion.
- `musicLibrary` - Custom module for managing music playback.
- `requests` - For making HTTP requests, e.g., fetching news.
- `openai` - For integrating with OpenAI's GPT-3.5-turbo.
- `gTTS` - For Google Text-to-Speech conversion.
- `pygame` - For playing audio files.
- `os` - For interacting with the operating system.

## Getting Started

### Prerequisites

Make sure you have Python installed. Install the required libraries by running:

```bash
pip install SpeechRecognition pyttsx3 requests openai gTTS pygame
```

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BasuKallapur/Python-source-code-CWH.git
    cd Python-source-code-CWH
    ```

2. **Replace API Keys:**

   - Insert your API key for [OpenAI](https://openai.com) in the code.
   - Insert your API key for [NewsAPI](https://newsapi.org) in the code.

3. **Run the Program:**

   ```bash
   python jarvis.py
   ```

### Usage

- Start the application and say **"Jarvis"** to activate the assistant.
- Use voice commands like:
  - **"Open Google"** to open the Google homepage.
  - **"Play [Song Name]"** to play a song.
  - **"News"** to get the latest news headlines.
  - Ask general questions to get responses via OpenAI.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [OpenAI](https://openai.com) for providing the GPT-3.5-turbo model.
- [NewsAPI](https://newsapi.org) for news data.
- All contributors and open-source library maintainers!

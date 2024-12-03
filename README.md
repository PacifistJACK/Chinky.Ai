# Chinky.AI  

**Chinky.AI** is an interactive voice assistant powered by speech recognition, text-to-speech technology, and a pre-trained LLaMA model via the Groq API. Chinky can perform a variety of tasks such as fetching news, telling the time or date, opening popular websites, and responding intelligently to user queries using AI.  

---

## Features  
- **Voice Command Recognition**: Listens to user commands via a microphone.  
- **AI-Powered Responses**: Utilizes LLaMA (via Groq API) for dynamic, intelligent answers.  
- **Personalized Assistance**: Performs tasks like opening websites, telling time, or fetching news headlines.  
- **Text-to-Speech Output**: Responds to users with a natural-sounding voice.  
- **Seamless Interaction**: Engages in continuous conversation until the user says "stop."  

---

## Technologies Used  
- **Python**: Core programming language for this project.  
- **SpeechRecognition**: For capturing and processing voice input.  
- **Pyttsx3**: For text-to-speech conversion.  
- **Webbrowser**: To open websites directly from voice commands.  
- **Requests**: To fetch live news from the NewsAPI.  
- **Groq API**: For integrating the LLaMA large language model.  
- **Datetime**: To fetch and format the current date and time.  

---

## Getting Started  

### Prerequisites  
- Python 3.8 or later  
- API keys for:  
  - **Groq API** (for LLaMA integration)  
  - **NewsAPI** (for fetching news headlines)  
- Microphone for voice input  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/chinky-ai.git
   cd chinky-ai

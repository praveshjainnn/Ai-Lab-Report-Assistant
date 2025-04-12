# AI Lab Report Assistant

This project allows students to generate structured lab reports using the Mistral-7B LLM via the OpenRouter API.

Follow the link to see the project on you tube : 
https://youtu.be/rpJoRzTF3xE?si=ecwg-iKp5_HKXpod

Prompt Documentation
a. Prompts Used:
Frontend Prompt
"Create a basic HTML page with internal CSS and JavaScript that interacts with a Flask API endpoint to submit user input and display the server's response."

Backend Prompt
"Write a simple Flask backend in Python that defines an API route (/process) to accept POST requests with JSON data and return a JSON response."

API Integration Prompt
"Modify the JavaScript in the HTML page to send an asynchronous fetch request to the Flask backend's /process endpoint and handle the response."

b. Brief Explanation of Design:
Prompt 1 (Frontend):
Focused on creating a self-contained UI using internal CSS/JS, making the project easy to deploy and test without external dependencies. It ensures modularity for small-scale projects or prototypes.

Prompt 2 (Backend):
Sets up a minimal Flask API, making it simple for beginners to understand request handling, JSON parsing, and response generation.

Prompt 3 (Integration):
This bridges the frontend and backend using AJAX/fetch API, which is essential in any API-based application. It ensures real-time interaction and demonstrates asynchronous request handling clearly.


## Features
- Frontend: HTML, CSS, JavaScript (Vanilla)
- Backend: Python with Flask
- LLM API: OpenRouter using Mistral-7B
- PDF Export using jsPDF
- Simulated login interface
- Secure API key handling via `.env`

## How to Run

1. Install requirements:
```
pip install -r requirements.txt
```

2. Create a `.env` file:
```
OPENROUTER_API_KEY=your-api-key-here
```

3. Start the Flask server:
```
python app.py
```

4. Open `index.html` in browser or host via a local web server.

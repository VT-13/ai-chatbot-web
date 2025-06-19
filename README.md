# AI Customer Service Chatbot

## How to Use

1. Clone or upload this project to GitHub.

2. To run locally:
- Install dependencies:
```
pip install flask openai
```
- Set your OpenAI API key:
```
export OPENAI_API_KEY="your_api_key_here"
```
- Run the server:
```
python app.py
```
- Open `index.html` in your browser.

3. To deploy:
- Use [Render](https://render.com/) for the backend (Flask).
- Use [Netlify](https://www.netlify.com/) for the frontend (static site).

## Chatbot Features

- Answers customer questions using a custom FAQ.
- Uses OpenAI's GPT model for natural responses.

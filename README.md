# Customer Support Chatbot — Flask Prototype

A small web application exploring FAQ-guided conversational support. A browser chat interface sends questions to a Python backend, which combines the question with a short support FAQ before requesting a generated answer.

## Implemented components

- HTML, CSS, and JavaScript chat interface with keyboard submission.
- Flask `POST /chat` endpoint accepting a JSON `message` field.
- Prompt construction using example shipping, refund, and warranty policies.
- Response rendering and basic request-failure messaging.
- Server-side API-key configuration through `OPENAI_API_KEY`.

## Architecture

```text
Browser chat interface → Flask /chat endpoint → language-model API
                             ↑
                       embedded FAQ
```

## Current status

This repository is an early prototype, not a deployment-ready service. The backend currently calls `openai.Completion.create` with `text-davinci-003`; the integration requires migration before a working demonstration with a current API can be claimed. Dependencies are unpinned, and the Flask application does not currently serve `index.html`.

Opening the HTML file directly is insufficient: its relative `/chat` request requires the frontend and backend to share an origin or an explicitly configured proxy.

## Source guide

| File | Purpose |
| --- | --- |
| `app.py` | FAQ, prompt construction, API request, and Flask route |
| `index.html` | Chat interface and browser request handling |
| `requirements.txt` | Python dependency list |

## Development priorities

1. Migrate the language-model request and pin compatible dependencies.
2. Serve the frontend and API under one origin.
3. Validate requests and handle errors without exposing internal details.
4. Add tests for FAQ handling, invalid input, and upstream failures.

The example support policies are demonstration data. The project does not establish answer accuracy, production reliability, or use by real customers.

from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

FAQ = {
    "shipping": "Our standard shipping takes 3-5 business days. Expedited options are available.",
    "refund": "You can request a refund within 30 days of purchase if the product is unused.",
    "warranty": "All products come with a one-year warranty covering manufacturing defects.",
}

def create_prompt(user_msg):
    faq_text = "\n".join([f"Q: {q}\nA: {a}" for q, a in FAQ.items()])
    prompt = (
        "You are a helpful customer service assistant. Use the FAQ below to answer questions.\n"
        f"{faq_text}\n"
        f"Customer: {user_msg}\n"
        "Assistant:"
    )
    return prompt

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    prompt = create_prompt(user_msg)

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            n=1,
            stop=["Customer:", "Assistant:"]
        )
        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": "Sorry, I couldn't process that request.", "error": str(e)}), 500

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)


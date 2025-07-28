from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Health Check route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Momager AI backend is live and sparkling!"})

# Route 1: Generate mood response
@app.route('/generate-mood', methods=['POST'])
def generate_mood():
    data = request.get_json()
    mood = data.get("mood")

    prompt = f"Respond like a glamorous, caring, sassy AI mom giving love and advice to someone who is feeling {mood}. Keep it short, warm, and very mom-like."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    mood_response = response['choices'][0]['message']['content']
    return jsonify({"response": mood_response})

# Route 2: Generate pep talk
@app.route('/generate-motivation', methods=['POST'])
def generate_motivation():
    prompt = "Give me a short, powerful pep talk from a sassy, loving, AI mom. Keep it under 4 lines and hype the user up."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    pep = response['choices'][0]['message']['content']
    return jsonify({"motivation": pep})
# Route 3: Venting comfort
@app.route('/generate-vent-response', methods=['POST'])
def generate_vent_response():
    data = request.get_json()
    vent = data.get("vent")

    prompt = f"Respond like a gentle, warm AI mom who is listening to someone say: '{vent}'. Offer short, empathetic support and love."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
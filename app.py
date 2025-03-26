from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://hook.eu2.make.com/ol13cdwj0qzpob4crnfbfkoese0soijp"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({"error": "Aucun message fourni"}), 400

    payload = {"message": user_input}

    try:
        response = requests.post(WEBHOOK_URL, json=payload)

        print("Webhook Response Status:", response.status_code)
        print("Webhook Response Content:", response.text)

        if response.status_code == 200:
           
            response_text = response.text
            
            
            code_start = response_text.find("```python") + 10
            code_end = response_text.find("```", code_start)
            code = response_text[code_start:code_end].strip()

            
            explanation_marker = "**Explication** :"
            explanation_start = response_text.find(explanation_marker)
            
            if explanation_start != -1:
               
                explanation_start += len(explanation_marker)
                
                
                explanation = response_text[explanation_start:].strip()
            else:
                explanation = "Aucune explication disponible."

            return jsonify({
                "code": code,
                "explanation": explanation
            })

        else:
            return jsonify({"error": "Échec de l'envoi", "status_code": response.status_code})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5001)

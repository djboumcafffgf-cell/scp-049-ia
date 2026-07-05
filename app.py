from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Assure-toi de configurer ta clé API en variable d'environnement sur Render
genai.configure(api_key=os.environ.get("API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Message manquant"}), 400
        
        user_msg = data['message']
        contexte = data.get('contexte', 'SCP-049 en patrouille')
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Contexte: {contexte}. Joueur dit: {user_msg}. Réponds en tant que SCP-049.")
        
        # On s'assure de retourner un JSON propre
        return jsonify({"reponse": response.text})
        
    except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({"reponse": "..."}), 200 # On renvoie un truc pour éviter le bug visuel

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

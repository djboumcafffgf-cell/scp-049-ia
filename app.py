from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Utilise la variable d'environnement pour plus de sécurité
genai.configure(api_key=os.environ.get("API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message_joueur = data.get("message")
    
    # Modele rapide et gratuit pour le jeu
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Instruction de comportement pour l'IA
    system_instruction = "Tu es le SCP-049. Reponds en francais, sans aucun accent (remplace les par des lettres standard). Ton ton doit rester froid, clinique et mysterieux."
    
    reponse = model.generate_content(f"{system_instruction} Le joueur dit : {message_joueur}")
    
    return jsonify({"reponse": reponse.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

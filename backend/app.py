from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilita CORS para permitir que o Angular (porta 4200) fale com o Python (porta 5000)
CORS(app)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # Se for descriptografar, invertemos o shift
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Verifica se é letra maiúscula
        if char.isupper():
            # A fórmula: (código_char + shift - código_A) % 26 + código_A
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Verifica se é letra minúscula
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Mantém espaços e pontuação inalterados
            result += char
    return result

@app.route('/cipher', methods=['POST'])
def cipher():
    data = request.json
    text = data.get('text', '')
    shift = int(data.get('shift', 0))
    mode = data.get('mode', 'encrypt') # 'encrypt' ou 'decrypt'
    
    processed_text = caesar_cipher(text, shift, mode)
    
    return jsonify({
        "original": text,
        "result": processed_text,
        "shift": shift,
        "mode": mode
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
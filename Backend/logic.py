from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12, include_upper=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    characters += string.ascii_lowercase  # always include lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_lowercase  # fallback

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/generate', methods=['GET'])
def generate():
    try:
        length = int(request.args.get('length', 12))
        include_upper = request.args.get('upper', 'true').lower() == 'true'
        include_numbers = request.args.get('numbers', 'true').lower() == 'true'
        include_symbols = request.args.get('symbols', 'true').lower() == 'true'

        if length < 8 or length > 64:
            return jsonify({'error': 'Length must be between 8 and 64'}), 400

        password = generate_password(length, include_upper, include_numbers, include_symbols)
        return jsonify({'password': password})
    except ValueError:
        return jsonify({'error': 'Invalid parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)